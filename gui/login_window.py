from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
import os
from backend.database import PasswordDatabase
from src.loginwindow_ui import Ui_LoginWindowUI
from gui.password_strength_indicator import PasswordStrengthIndicator
from gui.dialog_popup import DialogPopup
from backend.password_strength_logic import evaluate_password_strength
from config import Styles, resource_path, VERSION_NUM, IS_DEBUGGING, PopupType
import utils

class LoginWindow(QWidget):
    login_success = Signal(object)

    def __init__(self):
        super().__init__()
        self.db = PasswordDatabase()
        self.BASE_DIR = utils.DATA_PATH
        self.VAULT_PATH = utils.VAULT_PATH
        self.is_first_run = not os.path.exists(self.VAULT_PATH)
        
        # Load UI
        self.ui = Ui_LoginWindowUI()
        self.ui.setupUi(self)
        self.setStyleSheet(Styles.dark_style)
        self.apply_styles()
        footer_text = f"PassTreasure v{VERSION_NUM} © S3R43o3 2025"
        self.ui.footer_label.setText(f"{footer_text}")
        self.strength_indicator = PasswordStrengthIndicator(self)
        self.ui.indicatorHolder.addWidget(self.strength_indicator)
        
        # Shortcuts for easier access
        self.input_pw = self.ui.input_password
        self.label = self.ui.label_title
        self.error_label = self.ui.label_error
        self.btn_login = self.ui.btn_login
        self.btn_create = self.ui.btn_create
        
        pixmap = QPixmap(":/assets/icon.png")
        pixmap = pixmap.scaled(100, 100)
        self.ui.label_icon.setPixmap(pixmap)
        
        self.input_pw.setFocus()
        self._pw_visible = False
        self._pw2_visible = False
        
        self.configure_mode()
        self.ui.btn_toggle_pw.font().setPointSize(18)
        self.ui.btn_toggle_pw.setText("👁️")
        self.ui.btn_toggle_pw2.font().setPointSize(18)
        self.ui.btn_toggle_pw2.setText("👁️")
        self.ui.input_password2.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.btn_toggle_pw.clicked.connect(lambda checked, b=self.ui.btn_toggle_pw: self.toggle_password_visibility(b))
        self.ui.btn_toggle_pw2.clicked.connect(lambda checked, b=self.ui.btn_toggle_pw2: self.toggle_password_visibility(b))

        self.ui.btn_delete_vault.clicked.connect(self.handle_delete_vault)
        self.input_pw.returnPressed.connect(self.on_enter)
        self.input_pw.textChanged.connect(self._update_strength)        
        self.ui.input_password2.returnPressed.connect(self.on_enter)
        self.ui.btn_restore_backup.clicked.connect(self._restore_backup)
        
        if IS_DEBUGGING:
            self.input_pw.setText("kekskeks")
            self.ui.input_password2.setText("kekskeks")

    def apply_styles(self):
        self.ui.btn_login.setStyleSheet(Styles.green_button_outlined)
        self.ui.btn_delete_vault.setStyleSheet(Styles.red_button_outlined)
        self.ui.btn_create.setStyleSheet(Styles.green_button_outlined)
        self.ui.btn_toggle_pw.setStyleSheet(Styles.dark_button)
        self.ui.btn_restore_backup.setStyleSheet(Styles.yellow_button_outlined)            
        self.ui.btn_toggle_pw2.setStyleSheet(Styles.dark_button)
        utils.colorize_icon(self.ui.btn_login, "login", "green")
        utils.colorize_icon(self.ui.btn_delete_vault, "trash", "red")   
        utils.colorize_icon(self.ui.btn_create, "magic", "green")
        utils.colorize_icon(self.ui.btn_restore_backup, "reset", "yellow");                      
    
    def _update_strength(self):
        pw = self.ui.input_password.text()
        level = evaluate_password_strength(pw)
        self.strength_indicator.set_strength(level)
                
    def configure_mode(self): 
        if self.db.get_latest_backup():
            self.ui.btn_restore_backup.show()
        else:
            self.ui.btn_restore_backup.hide()
        if self.is_first_run:
            self.label.setText("Create Master Password:")
            self.btn_login.hide()
            self.btn_create.show()
            self.ui.pw2Frame.show()
            self.strength_indicator.show()
            self.ui.btn_delete_vault.hide()
            self.btn_create.clicked.connect(self.handle_create)
        else:
            self.label.setText("Enter Master Password:")
            self.btn_create.hide()
            self.strength_indicator.hide()
            self.btn_login.show()
            self.ui.pw2Frame.hide()
            self.ui.btn_delete_vault.show()
            self.btn_login.clicked.connect(self.handle_login)

        self.error_label.setText("")
    
    def _restore_backup(self):
        confirm = QMessageBox.question(self, "Confirm Restore Backup", "Are you sure to restore the backup?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:
            self.db.apply_backup(self.db.get_latest_backup())
            self.is_first_run = not os.path.exists(self.VAULT_PATH)
            self.configure_mode()

            DialogPopup("Backup Success", f"Backup restored successfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Backup Error", f"Failure restoring backup:\n{e}", PopupType.ERROR, self).exec()        
  

    def handle_delete_vault(self):
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this vault?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:        
            self.db.delete_vault()
            self.is_first_run = not os.path.exists(self.VAULT_PATH)
            self.configure_mode()
            DialogPopup("Vault Success", f"Vault deleted successfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Vault Error", f"Failure deleting vault:\n{e}", PopupType.ERROR, self).exec()        

    def handle_create(self):
        pw = self.input_pw.text().strip()
        pw2 = self.ui.input_password2.text().strip()
        if len(pw) < 6:
            self.error_label.setText("Password must be at least 6 characters!")
            return
        
        if pw != pw2:
            self.error_label.setText("Password didnt match!")
            return

        try:
            self.db.create_new_vault(pw)
        except Exception as e:
            DialogPopup("Vault Error", f"Failure creating vault:\n{e}", PopupType.ERROR, self).exec()        
            return

        self.is_first_run = not os.path.exists(self.VAULT_PATH)
        self.configure_mode()
        DialogPopup("Vault Success", "Vault created successfully!", PopupType.SUCCESS, self).exec()        
        self.login_success.emit(self.db)
        self.close()

    def handle_login(self):
        pw = self.input_pw.text().strip()

        if len(pw) < 6:
            self.error_label.setText("Password must be at least 6 characters!")
            return

        if self.db.unlock_vault(pw):
            self.login_success.emit(self.db)
            self.close()
        else:
            self.error_label.setText("Wrong password!")
    
    def toggle_password_visibility(self, button):
        if button == self.ui.btn_toggle_pw:
            self._pw_visible = not self._pw_visible
            if self._pw_visible:
                self.input_pw.setEchoMode(QLineEdit.EchoMode.Normal)
                self.ui.btn_toggle_pw.setText("🙈") 
            else:
                self.input_pw.setEchoMode(QLineEdit.EchoMode.Password)
                self.ui.btn_toggle_pw.setText("👁️")

        elif button == self.ui.btn_toggle_pw2:
            self._pw2_visible = not self._pw2_visible
            if self._pw2_visible:
                self.ui.input_password2.setEchoMode(QLineEdit.EchoMode.Normal)
                self.ui.btn_toggle_pw2.setText("🙈")   
            else:
                self.ui.input_password2.setEchoMode(QLineEdit.EchoMode.Password)
                self.ui.btn_toggle_pw2.setText("👁️") 

    def on_enter(self):
        if self.is_first_run:
            self.handle_create()
        else:
            self.handle_login()