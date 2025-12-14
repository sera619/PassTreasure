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
        self._build_ui()
        self.play_system_sound()
        self._fill_data()
        
    def _build_ui(self):
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        yes_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Yes)
        no_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.No)
        if ok_button:
            ok_button.setStyleSheet(config.Styles.green_button_outlined)
            utils.colorize_icon(ok_button, "check", "green")
        if yes_button:
            yes_button.setStyleSheet(config.Styles.green_button_outlined)
            utils.colorize_icon(yes_button, "check", "green")
            yes_button.clicked.connect(lambda: self.accept())
        if cancel_button:
            cancel_button.setStyleSheet(config.Styles.red_button_outlined)
            utils.colorize_icon(cancel_button, "close", "red")
        if no_button:
            no_button.setStyleSheet(config.Styles.red_button_outlined)
            utils.colorize_icon(no_button, "close", "red")
            no_button.clicked.connect(lambda: self.reject())
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
            case PopupType.QUESTION:
                winsound.MessageBeep(winsound.MB_OK)
    
    def _apply_mode(self):
        """Sets icon, colors, etc. based on popup mode."""
        match self.mode:
            case PopupType.SUCCESS:
                self.setWindowTitle("Success")
                icon = QPixmap(":/assets/check_circle.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#49d655"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #49d655;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok )
                
            case PopupType.INFO:
                self.setWindowTitle("Information")
                icon = QPixmap(":/assets/info.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#66b8f3"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #6fbdf5;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok # | QDialogButtonBox.StandardButton.Cancel
                                                     )

            case PopupType.WARNING:
                self.setWindowTitle("Warning")
                icon = QPixmap(":/assets/warn.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#f1bd54"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #f1bd54;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
                self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setAutoDefault(True)

            case PopupType.ERROR:
                self.setWindowTitle("Error")
                icon = QPixmap(":/assets/error.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#df2b2b"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #df2b2b;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
                self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setAutoDefault(True)

            case PopupType.QUESTION:
                self.setWindowTitle("Question")
                icon = QPixmap(":/assets/question.png")
                icon_colored = utils.tint_pixmap(icon, QColor("#58d6fc"))
                self.ui.iconLabel.setPixmap(icon_colored)
                self.ui.titleLabel.setStyleSheet("font: bold 15pt Segoe UI; color: #58d6fc;")
                self.ui.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Yes | QDialogButtonBox.StandardButton.No)
                self.ui.buttonBox.button(QDialogButtonBox.StandardButton.No).setAutoDefault(True)
