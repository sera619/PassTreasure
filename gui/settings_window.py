from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog, QLineEdit
from src.settingswindow_ui import Ui_SettingsWindow
import resources_rc
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Signal
from datetime import datetime

from config import ABOUT_TEXT, load_settings, save_settings, format_last_backup
from backend.database import PasswordDatabase

class SettingsWindow(QDialog):
    backup_restored = Signal(object)
    def __init__(self, db: PasswordDatabase):
        super().__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.db = db
        self.mapping = ["none", "daily", "weekly", "monthly", "yearly"]
        self.setup_navigation()
        self.setup_about_page()
        self.setWindowTitle("PassTreasure - Settings")
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        # Master password change
        self.ui.btn_apply_pw.clicked.connect(self.apply_master_pw)
        self.ui.btnCreateBackup.clicked.connect(self.create_new_backup)
        self.ui.btnRestoreBackup.clicked.connect(self.restore_backup)
        self.ui.btnDeleteBackup.clicked.connect(self.delete_backup)
        self.ui.btnClearBackup.clicked.connect(self.clear_backups)
        self.setup_general_page()
    
    def setup_general_page(self):
        settings = load_settings()
        for mode in self.mapping:
            self.ui.backupModeBox.addItem(mode.capitalize())
        mode = settings.get("auto_backup", "none")
        idx = {
            "none": 0,
            "daily": 1,
            "weekly": 2,
            "monthly": 3,
            "yearly": 4
        }.get(mode, 0)
        self.ui.backupModeBox.setCurrentIndex(idx)
        self.ui.backupModeBox.currentIndexChanged.connect(self.update_backup_mode)
        self.update_general_page()
    
    def update_backup_mode(self, index):
        mode = self.mapping[index]
        settings = load_settings()
        settings["auto_backup"] = mode
        save_settings(settings)
        QMessageBox.information(self, "Backup Setting", f"Automatic backups set to: {mode}")
        
    def update_general_page(self):
        lates_backup = self.db.get_latest_backup()
        if lates_backup:
            self.ui.btnDeleteBackup.setVisible(True)
            self.ui.btnRestoreBackup.setVisible(True)
            settings = load_settings()
            last_backup_raw = settings.get("last_backup")
            last_backup_time = format_last_backup(last_backup_raw)
            self.ui.backUpPathLabel.setText(f"{last_backup_time}")
            self.ui.btnClearBackup.show()
        else:
            self.ui.btnDeleteBackup.setVisible(False)
            self.ui.btnRestoreBackup.setVisible(False)
            self.ui.btnClearBackup.hide()
            self.ui.backUpPathLabel.setText("No Backups found!")            
            
    def create_new_backup(self):
        now = datetime.now()
        settings = load_settings()        
        self.db.create_backup()
        settings["last_backup"] = now.isoformat()
        save_settings(settings) 
        lates_backup = self.db.get_latest_backup()
        
        if not lates_backup:
            QMessageBox.critical(self, "Error", f"Cant find any backup!")
            return
        self.update_general_page()
        QMessageBox.information(self, "Success", f"Backup:\n{lates_backup}\n created successfully!")

    def restore_backup(self):
        lates_backup = self.db.get_latest_backup()
        if not lates_backup:
            QMessageBox.critical(self, "Error", f"Cant find any backup!")
            return
        confirm = QMessageBox.question(self, "Confirm Restore", "Are you sure you want to restore the backup?")
        if confirm != QMessageBox.Yes:
            return
        try:  
            self.db.apply_backup(lates_backup)
            self.db.reload_after_backup(self.ask_master_password)
            self.backup_restored.emit(self.db)
            QMessageBox.information(self, "Success", f"Backup:\n{lates_backup}\n restored successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to restore backup:\n{e}")
        
    def delete_backup(self):
        latest_backup = self.db.get_latest_backup()
        if latest_backup:
            confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this backup?")
            if confirm != QMessageBox.Yes:
                return
            try:        
                self.db.delete_backup(latest_backup)
                self.update_general_page()
                QMessageBox.information(self, "Success", f"Backup:\n{latest_backup}\n deleted successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete backup:\n{e}")
    
    def clear_backups(self):
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this backup?")
        if confirm != QMessageBox.Yes:
            return
        try:
            removed = self.db.clear_backups()
            self.update_general_page()      
            QMessageBox.information(self, "Success", f"{removed} backups deleted successfully!")
        except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete backup:\n{e}")

    def ask_master_password(self):        
        pw, ok = QInputDialog.getText(
            self,
            "Unlock Vault",
            "Enter master password:",
            echo=QLineEdit.EchoMode.Password
        )
        return pw if ok else None

    
    def setup_navigation(self):
        self.ui.btn_general.clicked.connect(
            lambda: self.ui.stack.setCurrentWidget(self.ui.page_general)
        )
        self.ui.btn_about.clicked.connect(
            lambda: self.ui.stack.setCurrentWidget(self.ui.page_about)
        )
        self.ui.btn_security.clicked.connect(
            lambda: self.ui.stack.setCurrentWidget(self.ui.page_security)
        )
    
    def apply_master_pw(self):
        old = self.ui.old_pw.text()
        new1 = self.ui.new_pw1.text()
        new2 = self.ui.new_pw2.text()

        if new1 != new2:
            QMessageBox.warning(self, "Error", "New passwords do not match!")
            return

        # Check old password
        if not self.db.unlock_vault(old):
            QMessageBox.warning(self, "Error", "Old password incorrect!")
            return

        try:
            self.db.change_master_password(new1)
            QMessageBox.information(self, "Success", "Master password updated!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            
    def setup_about_page(self):
        self.ui.aboutLabel.setText(ABOUT_TEXT)
        
        
        
        
        
        
        
        
        
        
        
        