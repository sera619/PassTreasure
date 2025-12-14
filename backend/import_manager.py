from PySide6.QtCore import QObject, QThread, Signal
from backend.import_worker import CsvImportWorker

class ImportManager(QObject):
    progress = Signal(int, int)
    finished = Signal()
    error = Signal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.thread: QThread | None = None
        self.worker: CsvImportWorker | None = None
        
    def start_import(self, vault_path: str, csv_path: str, master_pw: str, mode: str):
        if self.thread:
            return # prevent double starts
        
        self.thread = QThread()
        self.worker = CsvImportWorker(vault_path, csv_path, master_pw, mode)
        self.worker.moveToThread(self.thread)
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self._on_finished)
        self.worker.error.connect(self._on_error)        
        self.thread.started.connect(self.worker.run)
        self.thread.start()
        
    def _on_finished(self):
        self._clean_up()
        self.finished.emit()
    
    def _on_error(self, message: str):
        self._clean_up()
        self.error.emit(message)
        
    def _clean_up(self):
        if self.worker:
            self.worker.deleteLater()
            self.worker = None
        if self.thread:
            self.thread.quit()
            self.thread.wait()
            self.thread.deleteLater()
            self.thread = None