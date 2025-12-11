from PySide6.QtWidgets import QDialog, QColorDialog, QDialogButtonBox, QLineEdit
from PySide6.QtGui import QColor, QIcon
import resources_rc
import config
import utils

from src.edit_url_dialog_ui import Ui_EditUrlDialog


class EditURLDialog(QDialog):
    def __init__(self, service: str, old_url: str, parent = None):
        super().__init__(parent)
        self.service = service
        self.old_url = old_url
        self.ui = Ui_EditUrlDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.setWindowTitle("PassTreasure - Edit URL")
        self._build_ui()
        self._url: str = None        
        
    def _build_ui(self):
        self.ui.oldURLLabel.setText(self.old_url)
        self.ui.serviceLabel.setText(self.service)
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        self.ui.btnClearuURL.setStyleSheet(config.Styles.red_button_outlined)
        cancel_button.setStyleSheet(config.Styles.red_button_outlined)
        ok_button.setStyleSheet(config.Styles.green_button_outlined)
        utils.colorize_icon(ok_button, "check", "green")
        utils.colorize_icon(cancel_button, "close", "red")        
        utils.colorize_icon(self.ui.btnClearuURL, "close", "red")
        
        ok_button.clicked.disconnect()
        ok_button.clicked.connect(self._on_accept)
        cancel_button.clicked.disconnect()
        cancel_button.clicked.connect(self.reject)
        self.ui.btnClearuURL.clicked.connect(self.ui.newUrlLineEdit.clear)
        
    def _on_accept(self):
        new_url = self.ui.newUrlLineEdit.text().strip()
        if not new_url:
            return
        self._url = new_url
        self.accept()
    
    def get_url(self) -> str:
        return self._url