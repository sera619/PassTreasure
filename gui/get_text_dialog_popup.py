from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtCore import QSize
from src.get_text_dialog_popup_ui import Ui_GetTextDialogPopup
import resources_rc
from config import PopupType
import config
import utils


class GetTextDialogPopup(QDialog):
    def __init__(self, title: str, text: str, mode: str ="username", parent = None):
        super().__init__(parent)
        self.mode = mode
        self.title = title
        self.text = text
        self.ui = Ui_GetTextDialogPopup()
        self.ui.setupUi(self)
        self._value = ""
        self._build_ui()
        self._fill_data()
        
    def _build_ui(self):
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        self.ui.btnClearLineEdit.setStyleSheet(config.Styles.red_button_outlined)
        utils.colorize_icon(self.ui.btnClearLineEdit, "close", "red")
        ok_button.setStyleSheet(config.Styles.green_button_outlined)
        utils.colorize_icon(ok_button, "check", "green")
        cancel_button.setStyleSheet(config.Styles.red_button_outlined)
        utils.colorize_icon(cancel_button, "close", "red")

        self.ui.btnClearLineEdit.clicked.connect(self.ui.lineEdit.clear)
        ok_button.clicked.disconnect()
        ok_button.clicked.connect(self._on_accept)

        cancel_button.clicked.disconnect()
        cancel_button.clicked.connect(self.reject)
        self.ui.lineEdit.setPlaceholderText(f"Enter a {self.mode}...")
        self.setWindowTitle(f"Edit {self.mode.capitalize()}")
    
    def _fill_data(self):
        self.ui.titleLabel.setText(self.title)
        self.ui.textLabel.setText(self.text)
    
    def _on_accept(self):
        value = self.ui.lineEdit.text()
        if not value:
            return
        self._value = value
        self.accept()
        
    def get_value(self) -> str:
        return self._value