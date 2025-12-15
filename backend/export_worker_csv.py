# backend/export_worker_csv.py

from PySide6.QtCore import QObject, Signal
import csv


class CsvExportWorker(QObject):
    progress = Signal(int, int)
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, vault_path: str, export_path: str, master_pw):
        super().__init__()
        self.db_path = vault_path
        self.export_path = export_path
        self.master_pw = master_pw

    def run(self):
        from backend.database import PasswordDatabase

        try:
            db: PasswordDatabase = PasswordDatabase(self.db_path)
            db.connect()
            if not db.unlock_vault(self.master_pw):
                raise PermissionError("Invalid master password")
            
            entries = db.get_export_entries()
            field_names = entries[0].keys()
            total = len(entries)
            count = 0            
            
            with open(self.export_path, mode="w", newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                for entry in entries:
                    writer.writerow(entry)
                    count += 1
                    self.progress.emit(count, total)

            self.finished.emit(self.export_path)

        except Exception as e:
            self.error.emit(str(e))
