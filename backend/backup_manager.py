# backend/backup_manager.py

import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Optional

from utils import load_settings, save_settings


class BackupManager:
    """
    Central backup handling for PassTreasure.

    UI-facing responsibilities:
    - create backup
    - list backups
    - get latest backup
    - restore backup
    - auto-backup logic

    This class is filesystem-only. No sqlite connections here.
    """

    BACKUP_SUFFIX = "_vault.db"
    BACKUP_INTERVAL_TYPES = ["none", "daily", "weekly", "monthly", "yearly"]

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path).resolve()

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _backup_dir(self) -> Path:
        settings = load_settings()
        path = settings.get("backup_path")
        if not path:
            raise FileNotFoundError("backup_path not configured")
        p = Path(path).expanduser().resolve()
        p.mkdir(parents=True, exist_ok=True)
        return p
    
    def set_backup_path(self, new_path_str: str) -> bool:
        settings = load_settings()
        new_path = Path(new_path_str).expanduser().resolve()
        old_path = Path(settings.get("backup_path"))
        if old_path == new_path:
            return False
        old_backups = self.list_backups()
        settings["backup_path"] = str(new_path)
        save_settings(settings)
        new_path = self._backup_dir()
        
        if len(old_backups) > 0:
            moved = 0
            for old_backup_str in old_backups:
                try:
                    old_backup = old_path / old_backup_str
                    shutil.move(old_backup, new_path)
                    moved += 1
                    print(f"Move old Backup:\n{old_backup}")
                except Exception as e:
                    print(f"Error moving backup:\n{e}")
                    continue    
            print(f"Old backups moved: {moved}")         
        
        return True
    
    # ------------------------------------------------------------------
    # create
    # ------------------------------------------------------------------

    def create_backup(self) -> Path:
        if not self.vault_path.exists():
            raise FileNotFoundError("vault.db not found")

        ts = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        target = self._backup_dir() / f"{ts}{self.BACKUP_SUFFIX}"

        shutil.copy2(self.vault_path, target)

        settings = load_settings()
        settings["last_backup"] = ts
        save_settings(settings)

        return target

    # ------------------------------------------------------------------
    # list
    # ------------------------------------------------------------------

    def list_backups(self) -> List[str]:
        backups = []
        for f in self._backup_dir().iterdir():
            if f.is_file() and f.name.endswith(self.BACKUP_SUFFIX):
                backups.append(f.name)
        backups.sort(reverse=True)
        return backups

    def get_newest_backup(self) -> Optional[str]:
        backups = self.list_backups()
        backups.sort(reverse=True)
        return backups[0] if backups else None

    # ------------------------------------------------------------------
    # delete / clear 
    # ------------------------------------------------------------------

    def delete_backup(self, backup_filename: str):
        """
        Delete the selected backup file from the backup directory.
        """
        backup_dir = self._backup_dir()

        if not backup_dir.exists() or not backup_dir.is_dir():
            raise FileNotFoundError(f"Backup path does not exist: {backup_dir}")

        backup_file = backup_dir / backup_filename
        if not backup_file.exists():
            raise FileNotFoundError(f"Backup file not found: {backup_file}")

        backup_file.unlink()
        remaining = self.list_backups()
        if len(remaining) == 0:
            try:
                settings = load_settings()
                settings["last_backup"] = None
                save_settings(settings)
            except Exception as e:
                print(f"Failed to update settings: {e}")
                
    def clear_backups(self) -> Optional[int]:
        backup_dir = self._backup_dir()
        if not backup_dir.exists() or not backup_dir.is_dir():
            raise FileNotFoundError(f"Backup path does not exists: {backup_dir}")

        removed = 0
        for file in backup_dir.iterdir():
            if file.is_file() and file.name.endswith(self.BACKUP_SUFFIX):
                try: 
                    file.unlink()
                    removed += 1
                except Exception as e:
                    print(f"Failed to delete backup {file}:\n{e}")
        settings = load_settings()
        settings["last_backup"] = None
        save_settings(settings)
        return removed        
        
    # ------------------------------------------------------------------
    # restore
    # ------------------------------------------------------------------

    def restore_backup(self, filename: str) -> Path:
        src = self._backup_dir() / filename
        if not src.exists():
            raise FileNotFoundError(filename)

        if self.vault_path.exists():
            self.vault_path.unlink()

        shutil.copy2(src, self.vault_path)
        return self.vault_path

    # ------------------------------------------------------------------
    # auto backup
    # ------------------------------------------------------------------

    def auto_backup_if_needed(self) -> bool:
        settings = load_settings()
        enabled = settings.get("auto_backup", False)
        if not enabled:
            return False

        last = settings.get("last_backup")
        if last:
            try:
                ts = datetime.strptime(last, "%d-%m-%Y_%H-%M-%S")
                if (datetime.now() - ts).days < 1:
                    return False
            except Exception:
                pass

        self.create_backup()
        return True
