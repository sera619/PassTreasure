from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtCore import QSize, Qt
from src.dialog_popup_ui import Ui_DialogPopup
import resources_rc
from config import PopupType
import config
import utils
import winsound
    
class DialogPopup(QDialog):
    def __init__(self,
                 title: str, 
                 text: str, 
                 mode: PopupType = PopupType.INFO, 
                 parent = None):
        super().__init__(parent)
        self.ui = Ui_DialogPopup()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.title = title
        self.text = text
        self.mode: PopupType = mode
        self._apply_mode()
        self.play_system_sound()
        self._build_ui()
        self._fill_data()
        
    def _build_ui(self):
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button:
            ok_button.setStyleSheet(config.Styles.green_button_outlined)
            utils.colorize_icon(ok_button, "check", "green")
        if cancel_button:
            cancel_button.setStyleSheet(config.Styles.red_button_outlined)
            utils.colorize_icon(cancel_button, "close", "red")
        self.ui.textLabel.setStyleSheet("font: 10pt Segoe UI; color: #fff;")
        
    def _fill_data(self):
        self.ui.titleLabel.setText(self.title)
        self.ui.textLabel.setText(self.text)
    
    def play_system_sound(self):
        match self.mode:
            case PopupType.INFO:
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            case PopupType.SUCCESS:
                winsound.MessageBeep(winsound.MB_OK)
            case PopupType.ERROR:
                winsound.MessageBeep(winsound.MB_ICONHAND)
            case PopupType.WARNING:
                winsound.MessageBeep(winsound.MB_ICONHAND)
    
    def _apply_mode(self):
        """Sets icon, colors, etc. based on popup mode."""
        match self.mode:
            case PopupType.SUCCESS:
                self.setWindowTitle("Success")
                icon = QPixmap(":/assets/check_circle.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#49d655"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #49d655;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
                
            case PopupType.INFO:
                self.setWindowTitle("Information")
                icon = QPixmap(":/assets/info.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#6fbdf5"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #6fbdf5;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

            case PopupType.WARNING:
                self.setWindowTitle("Warning")
                icon = QPixmap(":/assets/warn.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#f1bd54"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #f1bd54;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

            case PopupType.ERROR:
                self.setWindowTitle("Error")
                icon = QPixmap(":/assets/error.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#df2b2b"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #df2b2b;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

