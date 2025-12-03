from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit
from src.change_password_dialog_ui import Ui_ChangePasswordDialog
from gui.passwordgenerator_popup import PasswordGeneratorPopup
import resources_rc

class ChangePasswordPopup(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_ChangePasswordDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        # Make sure both edits are in password mode (uic already sets this,
        # but it's harmless to enforce)
        self.ui.lineEditPassword1.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.lineEditPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        # Connect the dialog button box to the internal handlers
        self.ui.buttonBox.accepted.connect(self._on_accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        # store validated password here after OK
        self._password = None

        # Optional: small UX nicety — clear error when user types
        self.ui.lineEditPassword1.textChanged.connect(self._clear_error)
        self.ui.lineEditPassword2.textChanged.connect(self._clear_error)
        self.ui.btnGeneratePw.clicked.connect(self._open_generator)
        self.ui.check_show_pass.toggled.connect(self._on_toggle_show)
    
    def _open_generator(self):
        dialog = PasswordGeneratorPopup(parent=self)
        if dialog.exec():
            pw = dialog.get_password()
            self.ui.lineEditPassword1.setText(pw)
            self.ui.lineEditPassword2.setText(pw)
            
    
    def _clear_error(self, _=None):
        self.ui.labelError.setText("")
        
    def _on_accept(self):
        pw1 = self.ui.lineEditPassword1.text()
        pw2 = self.ui.lineEditPassword2.text()
        
        if not pw1 or not pw2:
            self.ui.labelError.setText("Please fill both fields.")
            return
        
        if pw1 != pw2:
            self.ui.labelError.setText("Passwords do not match.")
            return
        
        if len(pw1) < 6:
            self.ui.labelError.setText("Password must be at least 6 characters.")
            return
        
        self._password = pw1
        self.accept()
    
    def _on_toggle_show(self, checked: bool):
        mode = QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        self.ui.lineEditPassword1.setEchoMode(mode)
        self.ui.lineEditPassword2.setEchoMode(mode)
    
    def get_password(self) -> str:
        return self._password