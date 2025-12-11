from PySide6.QtCore import QObject, Signal
from utils import clean_url


class CsvImportWorker(QObject):
    progress = Signal(int, int)
    finished = Signal()
    error = Signal(str)

    def __init__(self, db_path, csv_path, master_pw: str, mode):
        super().__init__()
        self.db_path = db_path
        self.csv_path = csv_path
        self.mode = mode
        self.master_pw = master_pw

    def run(self):
        import csv
        from backend.database import PasswordDatabase
        try:
            db = PasswordDatabase(self.db_path)
            db.connect()
            db.unlock_vault(self.master_pw)
            
            with open(self.csv_path, "r", encoding="utf-8") as f:
                reader = list(csv.DictReader(f))

            total = len(reader)
            count = 0

            for row in reader:
                if self.mode == "firefox":                                        
                    service = clean_url(row.get("url")) or ""
                    username = row.get("username") or row.get("login") or ""
                    password = row.get("password") or ""
                    category = row.get("category") or "General"
                    url = row.get("url") or ""
                    note = row.get("note") or "" 
                elif self.mode == "chrome":
                    service = row.get("name") or ""
                    username = row.get("username") or ""
                    password = row.get("password") or ""
                    category = row.get("category") or "General"
                    url = row.get("url") or ""
                    note = row.get("note") or ""                     
                elif self.mode == "passtreasure":
                    # id,service,username,password,category,url,note
                    service = row.get("service") or ""
                    username = row.get("username") or ""
                    password = row.get("password") or ""
                    category = row.get("category") or "General"
                    url = row.get("url") or ""
                    note = row.get("note") or ""                     

                if password:
                    db.add_entry(service, username, password, category, url, note)

                count += 1
                self.progress.emit(count, total)

            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))
