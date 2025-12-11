from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTextEdit
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtCore import QEvent
import resources_rc
import config
import utils
from src.edit_note_dialog_ui import Ui_EditNoteDialog


class EditNoteDialog(QDialog):
    def __init__(self, service: str, old_note: str, parent = None):
        super().__init__(parent)
        self.service = service
        self.old_note = old_note
        self._note: str = ""          
        self.ui = Ui_EditNoteDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.setWindowTitle("PassTreasure - Edit Note")
        self._build_ui()
    
    def _build_ui(self):
        self.ui.serviceLabel.setText(self.service)
        self.ui.noteTextEdit.setText(self.old_note)
        cursor = self.ui.noteTextEdit.textCursor()
        
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.ui.noteTextEdit.setTextCursor(cursor)
        
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        ok_button.setStyleSheet(config.Styles.green_button_outlined)
        cancel_button.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnCleatNote.setStyleSheet(config.Styles.red_button_outlined)
        utils.colorize_icon(ok_button, "check", "green")
        utils.colorize_icon(cancel_button, "close", "red")        
        utils.colorize_icon(self.ui.btnCleatNote, "close", "red")
        
        ok_button.clicked.disconnect()
        ok_button.clicked.connect(self._on_accept)
        cancel_button.clicked.disconnect()
        cancel_button.clicked.connect(self.reject)
        ok_button.setFocus()
        self.ui.btnCleatNote.clicked.connect(self.ui.noteTextEdit.clear)
    
    def _on_accept(self):
        new_note = self.ui.noteTextEdit.toPlainText()
        self._note = new_note
        self.accept()
    
    def get_note(self) -> str:
        return self._note
        