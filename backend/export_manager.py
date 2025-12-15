# backend/export_manager.py

from PySide6.QtCore import QObject, QThread, Signal
from backend.export_worker_csv import CsvExportWorker


class ExportManager(QObject):
    progress = Signal(int, int)
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread: QThread | None = None
        self.worker: CsvExportWorker | None = None

    def start_export(self, vault_path:str, export_path: str, master_pw: str, export_type: str):
        if self.thread:
            return

        self.thread = QThread()

        if export_type == ".csv":
            self.worker = CsvExportWorker(vault_path, export_path, master_pw)
        else:
            raise ValueError(f"Unsupported export type: {export_type}")

        self.worker.moveToThread(self.thread)

        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self._on_finished)
        self.worker.error.connect(self._on_error)

        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def _on_finished(self, path: str):
        self._cleanup()
        self.finished.emit(path)

    def _on_error(self, msg: str):
        self._cleanup()
        self.error.emit(msg)

    def _cleanup(self):
        if self.worker:
            self.worker.deleteLater()
            self.worker = None
        if self.thread:
            self.thread.quit()
            self.thread.wait()
            self.thread.deleteLater()
            self.thread = None
