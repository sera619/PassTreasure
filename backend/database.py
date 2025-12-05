import sqlite3
import os
import random
import csv
from datetime import datetime, timezone 
from typing import Optional, List, Tuple
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from config import TEST_ENTRIES, resource_path, load_settings, save_settings, clean_url
import shutil
from backend.kdf import (
    generate_salt,
    derive_key,
    verify_master_password
)


DATA_PATH = resource_path('data')
BACKUP_PATH = resource_path('backup')
VAULT_PATH = resource_path('data/vault.db')

class PasswordDatabase:
    def __init__(self, path: str = VAULT_PATH):
        self.path = path
        self.conn = None
        self.cursor = None

        # AES key will be placed here after unlock
        self.aes_key: Optional[bytes] = None
        self._init_data()
        self._init_backup()
        

    def _init_backup(self):
        if not os.path.exists(BACKUP_PATH):
            os.makedirs(BACKUP_PATH)
            
    def _init_data(self):
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        load_settings()

    def add_test_entries(self) -> None:
        if self.aes_key is None:
            raise Exception("Vault not unlocked!")
        entries = TEST_ENTRIES
        
        for entry in entries:
            settings = load_settings()
            entry_categories = settings["entry_categories"]
            service = entry.get("service")
            username = entry.get("username")
            password = entry.get("password")
            url = entry.get("url", "https://www.google.com")
            category = entry.get("category", "General")
            category = random.choice(entry_categories)
            
            if not service or not username or not password:
                print(f"skipping invalid entry: {entry}")
                continue
            try:
                self.add_entry(service, username, password, category, url)
            except Exception as e:
                print(f"Failed to add entry: {e}")
            
    def connect(self) -> bool:
        if not os.path.exists(self.path):
            return False
        
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return True
    
    def disconnect(self) -> bool:
        if not self.conn:
            return False
        self.conn.close()
        self.conn = None
        self.cursor = None
        return True
    
    # Backup
    def create_backup(self):
        if not VAULT_PATH.exists():
            raise FileNotFoundError("vault.db does not exist – nothing to backup!")
        time_now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        backup_name = f"{time_now}_vault.db"
        backup_file = resource_path(f'backup/{backup_name}')
        shutil.copy2(VAULT_PATH, backup_file)
        return backup_file
    
    def get_latest_backup(self):
        backups = list(BACKUP_PATH.glob("*_vault.db"))
        if not backups:
            return None
        sorted_backups = sorted(backups, reverse=True)
        return sorted_backups[0].name
        
    def delete_backup(self, backup_filename: str):
        backup_file = BACKUP_PATH / backup_filename
        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file not found: {backup_file}")
        os.remove(backup_file)
        remaining = list(BACKUP_PATH.glob("*_vault.db"))
        if len(remaining) == 0:
            try:
                settings = load_settings()
                settings["last_backup"] = None
                save_settings(settings)
            except Exception as e:
                print(f"Failed to update settings: {e}")
    
    def clear_backups(self):
        if not BACKUP_PATH.exists():
            raise FileNotFoundError(f"Backup directory does not exists: {BACKUP_PATH}")
        removed = 0
        for file in BACKUP_PATH.iterdir():
            if file.is_file() and file.name.endswith("_vault.db"):
                try:
                    file.unlink()
                    removed += 1
                except Exception as e:
                    print(f"Failed to delete backup {file}: {e}")
        settings = load_settings()
        settings["last_backup"] = None
        save_settings(settings)
        return removed                        
    
    def apply_backup(self, backup_filename: str):
        backup_file = BACKUP_PATH / backup_filename
        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file not found: {backup_file}")
        # 1. Close DB connection if open
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass

        self.conn = None
        self.cursor = None
        self.aes_key = None

        if VAULT_PATH.exists():
            try:
                os.remove(VAULT_PATH)
            except PermissionError:
                raise PermissionError(
                    "vault.db is locked or in use! Close the application using it."
                )

        shutil.copy2(backup_file, VAULT_PATH)
        return VAULT_PATH

    def reload_after_backup(self, ask_password_callback=None):
        """
        Reloads the vault AFTER applying a backup.

        ask_password_callback → function that asks user for the master password
        (z.B. MainWindow.show_password_prompt() oder SettingsWindow Dialog)
        """

        # Connection + state reset (safety)
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass

        self.conn = None
        self.cursor = None
        self.aes_key = None

        # Vault wieder verbinden
        if not VAULT_PATH.exists():
            raise FileNotFoundError("Restored vault.db not found after backup!")

        if not self.connect():
            raise Exception("Could not connect to restored vault!")

        # ---- Unlock vault again ----
        if ask_password_callback is None:
            raise ValueError("Missing password callback function!")

        master_pw = ask_password_callback()
        if not master_pw:
            raise PermissionError("Vault reload aborted – no password entered.")

        if not self.unlock_vault(master_pw):
            raise PermissionError("Wrong master password for restored vault!")

        return True

    # Unlock / Verify
    def create_new_vault(self, master_password: str) -> None:
        if os.path.exists(self.path):
            raise Exception("Vault already exists!")

        salt = generate_salt()
        verifier_key = derive_key(master_password, salt)

        self.aes_key = verifier_key

        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()

        # META
        self.cursor.execute("""
            CREATE TABLE meta (
                id INTEGER PRIMARY KEY,
                salt BLOB NOT NULL,
                master_hash BLOB NOT NULL
            )
        """)

        # ENTRIES (jetzt mit category + timestamps!)
        self.cursor.execute("""
            CREATE TABLE entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password BLOB NOT NULL,
                url TEXT,
                nonce BLOB NOT NULL,
                category TEXT DEFAULT 'General',
                created_at TEXT,
                updated_at TEXT
            )
        """)

        self.cursor.execute(
            "INSERT INTO meta (id, salt, master_hash) VALUES (1, ?, ?)",
            (salt, verifier_key)
        )

        self.conn.commit()

    def change_master_password(self, old_password: str, new_password: str) -> bool:
        """
        Changes the master password securely.
        Steps:
        1. Verify old password
        2. Generate new salt + new hash
        3. Decrypt ALL entries using old aes_key
        4. Re-encrypt them using the new aes_key
        5. Write updated meta + entries back
        """
        # 1: Check old password
        if not self.unlock_vault(old_password):
            return False

        # Load existing encrypted entries
        self.cursor.execute("SELECT id, password, nonce FROM entries")
        rows = self.cursor.fetchall()

        # Decrypt all entries with old key
        aes_old = AESGCM(self.aes_key)
        decrypted_entries = []

        for entry_id, encrypted_pw, nonce in rows:
            pw = aes_old.decrypt(nonce, encrypted_pw, None).decode("utf-8")
            decrypted_entries.append((entry_id, pw))

        # 2: Generate new salt + derive new key
        new_salt = generate_salt()
        new_hash = derive_key(new_password, new_salt)
        new_aes_key = new_hash

        aes_new = AESGCM(new_aes_key)

        # 3: Re-encrypt all entries
        for entry_id, pw in decrypted_entries:
            new_nonce = os.urandom(12)
            new_enc = aes_new.encrypt(new_nonce, pw.encode("utf-8"), None)

            self.cursor.execute("""
                UPDATE entries
                SET password = ?, nonce = ?
                WHERE id = ?
            """, (new_enc, new_nonce, entry_id))

        # 4: Update meta table
        self.cursor.execute("""
            UPDATE meta
            SET salt = ?, master_hash = ?
            WHERE id = 1
        """, (new_salt, new_hash))
    
        self.conn.commit()

        # 5: Update runtime aes_key
        self.aes_key = new_aes_key
        return True

    def delete_vault(self) -> None:
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass
        
        self.conn = None
        self.cursor = None
        self.aes_key = None
        
        if not VAULT_PATH.exists():
            raise FileNotFoundError("vault.db does not exists - nothing to delete!")
        try:
            os.remove(VAULT_PATH)
        except PermissionError:
            raise PermissionError(
                "vault.db konnte nicht gelöscht werden — die Datei ist gesperrt!\n"
                "Schließe andere Programme oder Fenster, die darauf zugreifen."
            )

    def unlock_vault(self, master_password: str) -> bool:

        if not self.connect():
            return False

        self.cursor.execute("SELECT salt, master_hash FROM meta WHERE id = 1")
        row = self.cursor.fetchone()
        if row is None:
            return False

        salt, expected_key = row

        if verify_master_password(master_password, salt, expected_key):
            self.aes_key = derive_key(master_password, salt)
            return True

        return False

    # Password Entry Handling
    def add_entry(self, service: str, username: str, password: str, category: str = "General", url: str = "Unknown") -> None:

        if self.aes_key is None:
            raise Exception("Vault not unlocked!")

        aes = AESGCM(self.aes_key)
        nonce = os.urandom(12)
        encrypted_pw = aes.encrypt(nonce, password.encode("utf-8"), None)

        now = datetime.now(timezone.utc).isoformat()

        self.cursor.execute("""
            INSERT INTO entries (service, username, password, url, nonce, category, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (service, username, encrypted_pw, url, nonce, category, now, now))

        self.conn.commit()

    def get_entry_details(self, entry_id: int):
        """
        Returns full entry details including timestamps and category.
        """
        self.cursor.execute("""
            SELECT service, username, category, url, created_at, updated_at
            FROM entries
            WHERE id = ?
        """, (entry_id,))
        
        row = self.cursor.fetchone()
        if row is None:
            raise Exception("Entry not found!")

        service, username, category, url, created_at, updated_at = row
        return {
            "service": service,
            "username": username,
            "category": category,
            "url": url,
            "created_at": created_at,
            "updated_at": updated_at
        }

    def get_all_entries(self) -> List[Tuple[int, str, str, str]]:
        """Returns id, service, username, category for listing."""
        self.cursor.execute("SELECT id, service, username, category FROM entries")
        return self.cursor.fetchall()

    def get_password(self, entry_id: int) -> str:

        if self.aes_key is None:
            raise Exception("Vault not unlocked!")

        self.cursor.execute(
            "SELECT password, nonce FROM entries WHERE id = ?",
            (entry_id,)
        )
        row = self.cursor.fetchone()
        if row is None:
            raise Exception("Password entry not found!")

        encrypted_pw, nonce = row

        aes = AESGCM(self.aes_key)
        decrypted = aes.decrypt(nonce, encrypted_pw, None)

        return decrypted.decode("utf-8")

    def delete_entry(self, entry_id: int) -> None:

        self.cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        self.conn.commit()
    
    def get_entries_by_category(self, category: str) -> List[tuple]:
        """
        Returns all entries assigned to a specific category.
        """
        self.cursor.execute("""
            SELECT id, service, username, category
            FROM entries
            WHERE category = ?
        """, (category,))
        return self.cursor.fetchall()

    def clear_entries(self):
        self.cursor.execute("DELETE FROM entries")
        self.cursor.execute("DELETE FROM sqlite_sequence WHERE name='entries'")
        self.conn.commit()
        
    # UPDATE: Edit fields
    def edit_category(self,  entry_id: int, new_category: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.cursor.execute(
            "UPDATE entries SET category = ?, updated_at = ? WHERE id = ?",
            (new_category, now, entry_id)
        )
        self.conn.commit()
    
    def edit_service(self, entry_id: int, new_service: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.cursor.execute(
            "UPDATE entries SET service = ?, updated_at = ? WHERE id = ?",
            (new_service, now, entry_id)
        )
        self.conn.commit()

    def edit_username(self, entry_id: int, new_username: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.cursor.execute(
            "UPDATE entries SET username = ?, updated_at = ? WHERE id = ?",
            (new_username, now, entry_id)
        )
        self.conn.commit()

    def edit_password(self, entry_id: int, new_password: str) -> None:

        if self.aes_key is None:
            raise Exception("Vault not unlocked!")

        aes = AESGCM(self.aes_key)
        nonce = os.urandom(12)
        encrypted_pw = aes.encrypt(nonce, new_password.encode("utf-8"), None)

        now = datetime.now(timezone.utc).isoformat()

        self.cursor.execute("""
            UPDATE entries 
            SET password = ?, nonce = ?, updated_at = ?
            WHERE id = ?
        """, (encrypted_pw, nonce, now, entry_id))

        self.conn.commit()

    def edit_url(self, entry_id: int, new_url: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.cursor.execute(
            "UPDATE entries SET url = ?, updated_at = ? WHERE id = ?",
            (new_url, now, entry_id)
        )
        self.conn.commit()

    def update_entry(self, entry_id: int, service: str, username: str, password: str, category: str) -> None:

        if self.aes_key is None:
            raise Exception("Vault not unlocked!")

        aes = AESGCM(self.aes_key)
        nonce = os.urandom(12)
        encrypted_pw = aes.encrypt(nonce, password.encode("utf-8"), None)

        now = datetime.now(timezone.utc).isoformat()

        self.cursor.execute("""
            UPDATE entries
            SET service = ?, username = ?, password = ?, nonce = ?, category = ?, updated_at = ?
            WHERE id = ?
        """, (service, username, encrypted_pw, nonce, category, now, entry_id))

        self.conn.commit()


