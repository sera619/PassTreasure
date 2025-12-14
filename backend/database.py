# database.py – refactored (phase 1)
import os
import sqlite3
import random
import shutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Tuple, Dict

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from config import TEST_ENTRIES
from utils import load_settings, save_settings, get_base_dir
from backend.crypto_manager import CryptoManager
from backend.backup_manager import BackupManager
# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

BASE_DIR = get_base_dir()
DATA_PATH = os.path.join(BASE_DIR, "data")
BACKUP_PATH = os.path.join(BASE_DIR, "backup")
VAULT_PATH = os.path.join(DATA_PATH, "vault.db")


class PasswordDatabase:
    """
    Main database access layer for PassTreasure.

    Responsibilities (phase 1):
    - SQLite connection handling
    - Vault unlock / crypto usage
    - Entry CRUD
    - Backup handling
    - DB migrations

    NOTE: Further refactors may split this into smaller services.
    """

    # ------------------------------------------------------------------
    # INIT / STATE
    # ------------------------------------------------------------------

    def __init__(self, db_path: str = VAULT_PATH):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None
        self.aes_key: Optional[bytes] = None
        self.backup_manager: BackupManager = BackupManager(self.db_path)
        
        self._init_data_dirs()
        self._init_backup_dir()

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------

    def _utc_now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def _require_connected(self):
        if not self.conn or not self.cursor:
            raise RuntimeError("Database not connected")

    def _require_unlocked(self):
        """Check if aes_key exists"""
        if self.aes_key is None:
            raise RuntimeError("Vault not unlocked")

    def _execute(
        self,
        query: str,
        params: tuple = (),
        *,
        commit: bool = False,
        fetchone: bool = False,
        fetchall: bool = False,
    ):
        self._require_connected()
        self.cursor.execute(query, params)

        if commit:
            self.conn.commit()
        if fetchone:
            return self.cursor.fetchone()
        if fetchall:
            return self.cursor.fetchall()

    # ------------------------------------------------------------------
    # INIT DIRECTORIES
    # ------------------------------------------------------------------

    def _init_data_dirs(self):
        os.makedirs(DATA_PATH, exist_ok=True)
        load_settings()

    def _init_backup_dir(self):
        settings = load_settings()
        path = os.path.abspath(settings.get("backup_path"))
        os.makedirs(path, exist_ok=True)

    # ------------------------------------------------------------------
    # CONNECTION HANDLING
    # ------------------------------------------------------------------

    def connect(self) -> bool:
        if not os.path.exists(self.db_path):
            return False
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return True

    def disconnect(self) -> bool:
        if not self.conn:
            return False
        self.conn.close()
        self.conn = None
        self.cursor = None
        self.aes_key = None
        return True

    # ------------------------------------------------------------------
    # VAULT CREATION / AUTH
    # ------------------------------------------------------------------

    def create_new_vault(self, master_password: str) -> None:
        if os.path.exists(self.db_path):
            raise RuntimeError("Vault already exists")

        salt = CryptoManager.generate_salt()
        verifier_key = CryptoManager.derive_key(master_password, salt)
        self.aes_key = verifier_key

        self.connect()

        self.cursor.execute("""
            CREATE TABLE meta (
                id INTEGER PRIMARY KEY,
                salt BLOB NOT NULL,
                master_hash BLOB NOT NULL,
                db_version INTEGER DEFAULT 1
            )
        """)

        self.cursor.execute("""
            CREATE TABLE entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password BLOB NOT NULL,
                nonce BLOB NOT NULL,
                url TEXT,
                category TEXT DEFAULT 'General',
                note TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        """)

        self.cursor.execute(
            "INSERT INTO meta (id, salt, master_hash) VALUES (1, ?, ?)",
            (salt, verifier_key)
        )
        self.conn.commit()

    def unlock_vault(self, master_password: str) -> bool:
        if not self.connect():
            return False

        row = self._execute(
            "SELECT salt, master_hash FROM meta WHERE id = 1",
            fetchone=True
        )
        if row is None:
            return False

        salt, expected_key = row
        if not CryptoManager.verify_master_password(master_password, salt, expected_key):
            return False

        self.aes_key = CryptoManager.derive_key(master_password, salt)
        self.migrate_database()
        return True

    def change_master_password(self, old_password: str, new_password: str) -> bool:
        if not self.unlock_vault(old_password):
            return False

        rows = self._execute(
            "SELECT id, password, nonce FROM entries",
            fetchall=True
        )

        aes_old = AESGCM(self.aes_key)
        decrypted = [
            (eid, aes_old.decrypt(n, pw, None).decode("utf-8"))
            for eid, pw, n in rows
        ]

        new_salt = CryptoManager.generate_salt()
        new_key = CryptoManager.derive_key(new_password, new_salt)
        aes_new = AESGCM(new_key)

        for entry_id, pw in decrypted:
            nonce, enc = CryptoManager.encrypt(aes_new, pw.encode())
            # nonce = os.urandom(12)
            # enc = aes_new.encrypt(nonce, pw.encode(), None)
            self._execute(
                "UPDATE entries SET password=?, nonce=? WHERE id=?",
                (enc, nonce, entry_id)
            )

        self._execute(
            "UPDATE meta SET salt=?, master_hash=? WHERE id=1",
            (new_salt, new_key),
            commit=True
        )

        self.aes_key = new_key
        return True
 
    def apply_backup(self, backup_filename: str):
        settings = load_settings()
        backup_path_str = settings.get("backup_path")

        if not backup_path_str:
            raise FileNotFoundError("Backup path not configured.")

        backup_dir = Path(os.path.abspath(backup_path_str))

        if not backup_dir.exists() or not backup_dir.is_dir():
            raise FileNotFoundError(f"Backup path does not exist: {backup_dir}")  
         
        backup_file = backup_dir / backup_filename
        
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

        if os.path.exists(VAULT_PATH):
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
        if not os.path.exists(VAULT_PATH):
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
 
    # ------------------------------------------------------------------
    # ENTRY CRUD
    # ------------------------------------------------------------------

    def create_entry(self, service: str, username: str, password: str,
                  category: str = "General", url: str = "", note: str = ""):
        self._require_unlocked()

        # aes = AESGCM(self.aes_key)
        # nonce = os.urandom(12)
        # enc = aes.encrypt(nonce, password.encode(), None)
        
        nonce, enc = CryptoManager.encrypt(self.aes_key, password)       
        now = self._utc_now()

        self._execute(
            """
            INSERT INTO entries
            (service, username, password, nonce, url, category, note, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (service, username, enc, nonce, url, category, note, now, now),
            commit=True
        )

    def get_entry_details(self, entry_id: int) -> Optional[Dict]:
        """
        Returns full entry details:
        service, username, category, url, note, created_at, updated_at
        """
        row = self._execute("""
            SELECT service, username, category, url, note, created_at, updated_at
            FROM entries
            WHERE id = ?
            """, (entry_id,),
            fetchone=True
        )
        if row is None:
            raise Exception("Entry not found!")
        service, username, category, url, note, created_at, updated_at = row
        return {
            "service": service,
            "username": username,
            "category": category,
            "url": url,
            "note": note,
            "created_at": created_at,
            "updated_at": updated_at
        }

    def get_all_entries(self) -> List[Tuple[int, str, str, str]]:
        self._require_unlocked()
        return self._execute(
            "SELECT id, service, username, category FROM entries",
            fetchall=True
        )
        
    def get_entries_by_category(self, category: str) -> List[Tuple[int, str, str, str]]:
        """Returns all entries assigned to a specific category."""
        self._require_unlocked()
        return self._execute("""
            SELECT id, service, username, category
            FROM entries
            WHERE category = ?""",
            (category,),
            fetchall=True
        )
        
    def get_export_entries(self) -> list[dict]:
        """Returns id, service, username, password, url, category, note, created_at, updated_at
        """
        self._require_unlocked()
        rows = self._execute("""
            SELECT id, service, username, password, nonce, url, category, note, created_at, updated_at
            FROM entries""",
            fetchall=True
        )
        export = []
        for row in rows:
            (entry_id, service, username, 
                enc_pw, nonce, category, url,
                note, created_at, updated_at
            ) = row
            password = CryptoManager.decrypt(self.aes_key, nonce, enc_pw)
            export.append({
                "id": entry_id,
                "service": service,
                "username": username,
                "password": password,
                "category": category,
                "url": url,
                "note": note,
                "created_at": created_at,
                "updated_at": updated_at
            })
        return export        
    
    def get_password(self, entry_id: int) -> str:
        self._require_unlocked()
        row = self._execute(
            "SELECT password, nonce FROM entries WHERE id=?",
            (entry_id,),
            fetchone=True
        )
        if not row:
            raise KeyError("Entry not found")
        pw, nonce = row
        dec_pw = CryptoManager.decrypt(self.aes_key, nonce, pw)
        # AESGCM(self.aes_key).decrypt(nonce, pw, None).decode()
        return dec_pw

    def delete_entry(self, entry_id: int):
        self._require_unlocked()
        self._execute(
            "DELETE FROM entries WHERE id=?",
            (entry_id,),
            commit=True
        )
        remaining =  self.get_all_entries() 
        if len(remaining) == 0:
            self._execute(
                "DELETE FROM sqlite_sequence WHERE name='entries'", 
                commit=True
            )

    def clear_entries(self):
        self._require_unlocked()
        self._execute(
            "DELETE FROM entries"
        )
        self._execute(
            "DELETE FROM sqlite_sequence WHERE name='entries'",
            commit=True
        )

    def edit_category(self, entry_id: int, new_category: str) -> None:
        now = self._utc_now()
        self._execute(
            "UPDATE entries SET category = ?, updated_at = ? WHERE id = ?",
            (new_category, now, entry_id),
            commit=True
        )
        
    def edit_service(self, entry_id: int, new_service: str) -> None:
        now = self._utc_now()
        self._execute(
            "UPDATE entries SET service = ?, updated_at = ? WHERE id = ?",
            (new_service, now, entry_id),
            commit=True
        )

    def edit_username(self, entry_id: int, new_username: str) -> None:
        now = self._utc_now()        
        self._execute(
            "UPDATE entries SET username = ?, updated_at = ? WHERE id = ?",
            (new_username, now, entry_id),
            commit=True
        )

    def edit_password(self, entry_id: int, new_password: str) -> None:
        now = self._utc_now()        
        nonce, encrypted_pw = CryptoManager.encrypt(self.aes_key, new_password)
        self._execute("""
            UPDATE entries 
            SET password = ?, nonce = ?, updated_at = ?
            WHERE id = ?
            """, 
            (encrypted_pw, nonce, now, entry_id),
            commit=True
        )

    def edit_url(self, entry_id: int, new_url: str) -> None:
        now = self._utc_now()
        self._execute(
            "UPDATE entries SET url = ?, updated_at = ? WHERE id = ?",
            (new_url, now, entry_id),
            commit=True
        )
        
    def edit_note(self, entry_id: int, new_note: str) -> None:
        now = self._utc_now()
        self._execute(
            "UPDATE entries SET note = ?, updated_at = ? WHERE id = ?",
            (new_note, now, entry_id),
            commit=True
        )

    # ------------------------------------------------------------------
    # MIGRATION
    # ------------------------------------------------------------------

    def migrate_database(self):
        cols = [
            row[1]
            for row in self._execute("PRAGMA table_info(meta)", fetchall=True)
        ]
        if "db_version" not in cols:
            self._execute(
                "ALTER TABLE meta ADD COLUMN db_version INTEGER DEFAULT 1",
                commit=True
            )

    # ------------------------------------------------------------------
    # TEST DATA
    # ------------------------------------------------------------------

    def add_test_entries(self):
        self._require_unlocked()
        settings = load_settings()
        categories = settings.get("entry_categories", ["General"])

        for entry in TEST_ENTRIES:
            try:
                self.create_entry(
                    service=entry["service"],
                    username=entry["username"],
                    password=entry["password"],
                    category=random.choice(categories),
                    url=entry.get("url", ""),
                    note="No note"
                )
            except Exception as e:
                print(f"Test entry failed: {e}")
