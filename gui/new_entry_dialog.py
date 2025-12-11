from PySide6.QtWidgets import QDialog, QColorDialog, QDialogButtonBox, QLineEdit
from PySide6.QtGui import QColor, QIcon
import resources_rc
import config
import utils
from src.new_entry_dialog_ui import Ui_NewEntryDialog
from gui.passwordgenerator_popup import PasswordGeneratorPopup
from gui.password_strength_indicator import PasswordStrengthIndicator
from backend.password_strength_logic import evaluate_password_strength

class NewEntryDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_NewEntryDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.setWindowTitle("PassTreasure - New Entry")
        self._apply_style()
        self._build_ui()
        ok_btn = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_btn = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        ok_btn.clicked.disconnect()
        ok_btn.clicked.connect(self._on_accept)

        cancel_btn.clicked.disconnect()
        cancel_btn.clicked.connect(self.reject)
        
        # self.ui.buttonBox.rejected.connect(self.reject)
        # self.ui.buttonBox.accepted.connect(self._on_accept)
        
        self.strength_indicator = PasswordStrengthIndicator()
        self.ui.indicatorHolder.addWidget(self.strength_indicator)
        self.ui.pw1Input.textChanged.connect(self._update_strength)
        self.ui.btnGeneratePw.clicked.connect(self._open_generator)
        self.ui.pwVisibilityCheck.toggled.connect(self._on_toggle_show)
        self.entry_data = {}


    def _build_ui(self):
        settings = config.load_settings()
        categories = list(settings.get("entry_categories"))
        self.ui.categoryComboBox.addItems(categories)
        self.ui.labelError.setText("")

        self.ui.btnClearPw1.clicked.connect( self.ui.pw1Input.clear)
        self.ui.btnClearPw2.clicked.connect( self.ui.pw2Input.clear)
        self.ui.btnClearService.clicked.connect( self.ui.newServiceInput.clear)
        self.ui.btnClearUrl.clicked.connect( self.ui.urlInput.clear)
        self.ui.btnClearUsername.clicked.connect( self.ui.newUsernameInput.clear)
        self.ui.btnClearNote.clicked.connect(self.ui.noteTextEdit.clear)
        
        utils.colorize_icon(self.ui.btnClearPw1, "close", "red")
        utils.colorize_icon(self.ui.btnClearPw2, "close", "red")
        utils.colorize_icon(self.ui.btnClearService, "close", "red")
        utils.colorize_icon(self.ui.btnClearUrl, "close", "red")
        utils.colorize_icon(self.ui.btnClearUsername, "close", "red")
        utils.colorize_icon(self.ui.btnClearNote, "close", "red")
        
        self.ui.pw1Input.textChanged.connect(self._clear_error)
        self.ui.pw2Input.textChanged.connect(self._clear_error)
        self.ui.urlInput.textChanged.connect(self._clear_error)
        self.ui.newServiceInput.textChanged.connect(self._clear_error)
        self.ui.newUsernameInput.textChanged.connect(self._clear_error)
        
        self._on_toggle_show(False)

    def _clear_error(self, _=None):
        self.ui.labelError.setText("")
        
    def _update_strength(self):
        pw = self.ui.pw1Input.text()
        level = evaluate_password_strength(pw)
        self.strength_indicator.set_strength(level)
    
    def _open_generator(self):
        dialog = PasswordGeneratorPopup(parent=self)
        if dialog.exec():
            pw = dialog.get_password()
            self.ui.pw1Input.setText(pw)
            self.ui.pw2Input.setText(pw)

    def _on_toggle_show(self, checked: bool):
        mode = QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        self.ui.pw1Input.setEchoMode(mode)
        self.ui.pw2Input.setEchoMode(mode)

    def _apply_style(self):
        self.ui.btnGeneratePw.setStyleSheet(config.Styles.yellow_button_outlined)
        ok_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        self.ui.btnClearPw1.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnClearPw2.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnClearService.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnClearUrl.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnClearUsername.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.btnClearNote.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.line.setStyleSheet(config.Styles.h_line)
        self.ui.line_2.setStyleSheet(config.Styles.h_line)
        self.ui.line_3.setStyleSheet(config.Styles.h_line)
        self.ui.line_4.setStyleSheet(config.Styles.h_line)       
        self.ui.line_5.setStyleSheet(config.Styles.h_line)
        utils.colorize_icon(self.ui.btnClearPw1, "close", "red")
        utils.colorize_icon(self.ui.btnClearPw2, "close", "red")
        utils.colorize_icon(self.ui.btnClearService, "close", "red")
        utils.colorize_icon(self.ui.btnClearUrl, "close", "red")
        utils.colorize_icon(self.ui.btnClearUsername, "close", "red")
        utils.colorize_icon(self.ui.btnClearNote, "close", "red")
        utils.colorize_icon(self.ui.btnGeneratePw, "magic", "yellow")
                      
        if ok_button:
            ok_button.setStyleSheet(config.Styles.green_button_outlined)
            utils.colorize_icon(ok_button, "check", "green")
        if cancel_button:
            cancel_button.setStyleSheet(config.Styles.red_button_outlined)
            utils.colorize_icon(cancel_button, "close", "red")
    
    def _on_accept(self):
        service = self.ui.newServiceInput.text()
        if not service or service == "":
            self.ui.labelError.setText("Please enter a service!")
            return
        
        username = self.ui.newUsernameInput.text()
        if not username or username == "":
            self.ui.labelError.setText("Please enter a username!")
            return
        
        url = self.ui.urlInput.text()
        if not url or url  == "":
            self.ui.labelError.setText("Please enter a url!")
            return        
        
        pw1 = self.ui.pw1Input.text()
        pw2 = self.ui.pw2Input.text()
        if not pw1 or not pw2:
            self.ui.labelError.setText("Please fill both password fields.")
            return
        
        if pw1 != pw2:
            self.ui.labelError.setText("Passwords do not match.")
            return
        
        if len(pw1) < 6:
            self.ui.labelError.setText("Password must be at least 6 characters.")
            return
        
        category = self.ui.categoryComboBox.currentText()
        if not category:
            category = "General"
            
        note = self.ui.noteTextEdit.text()
        if not note:
            note = "No Note set."
        
        self.entry_data["service"] = service
        self.entry_data["username"] = username
        self.entry_data["password"] = pw1
        self.entry_data["url"] = url
        self.entry_data["category"] = category
        self.entry_data["note"] = note
        self.accept()
        
    def get_entry_data(self) -> dict:
        return self.entry_data