from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog, QLineEdit, QColorDialog, QPushButton, QVBoxLayout, QFileDialog
from src.settingswindow_ui import Ui_SettingsWindow
import resources_rc
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt, Signal, QTimer, QTime
from datetime import datetime
from gui.category_edit_dialog import CategoryEditDialog
from gui.password_strength_indicator import PasswordStrengthIndicator
from backend.password_strength_logic import evaluate_password_strength
from gui.dialog_popup import DialogPopup
from backend.import_worker import CsvImportWorker
from config import TextStorage, Styles, VAULT_PATH, PopupType, EXPORT_TYPES
from backend.database import PasswordDatabase
from utils import load_settings, save_settings, format_last_backup
import utils
import os, csv, json


class SettingsWindow(QDialog):
    backup_restored = Signal(object)
    category_deleted = Signal()
    category_updated = Signal()
    import_successfully = Signal()
    autologout_activated = Signal()
    autologout_deactivated = Signal()
    def __init__(self, db: PasswordDatabase):
        super().__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.db = db
        self.default_export_name = "FileTreasure-PasswordExport"
        self.mapping = ["none", "daily", "weekly", "monthly", "yearly"]
        self.new_category_color = None
        self.setup_navigation()
        self.setup_about_page()
        self.setup_import_page()
        self.setup_general_page()
        self.setup_export_page()
        self.setWindowTitle("PassTreasure - Settings")
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.apply_styles()
        
        # Master password change
        self.strength_indicator = PasswordStrengthIndicator(self)
        self.ui.indicatorHolder.addWidget(self.strength_indicator)        
        
        self.setup_edit_category()
        self.set_autologout_time()
        self.set_auto_hide_details_time()
        
        self.ui.new_pw1.textChanged.connect(self._update_pw_strength)
        self.ui.btn_apply_pw.clicked.connect(self.apply_master_pw)
        self.ui.btnCreateBackup.clicked.connect(self.create_new_backup)
        self.ui.btnRestoreBackup.clicked.connect(self.restore_backup)
        self.ui.btnDeleteBackup.clicked.connect(self.delete_backup)
        self.ui.btnClearBackup.clicked.connect(self.clear_backups)
        self.ui.showPwCheckbox.toggled.connect(self.toggle_masterpw_visibility)
        self.ui.btnStartImport.clicked.connect(self.start_import)
        self.ui.btnSelectPath.clicked.connect(self.get_import_path)
        self.ui.stack.currentChanged.connect(self.update_sidebar_buttons)
        
        self.ui.autoLogoutCheckBox.toggled.connect(self.toggle_autologout)
        self.ui.autoLogoutTimeEdit.timeChanged.connect(self.get_autologout_time)
        self.ui.autoHideDetailsTimeEdit.timeChanged.connect(self.get_auto_hide_details_time)
        self.ui.exportFilenameLineEdit.setPlaceholderText(f"Enter a filename... (default: {self.default_export_name})")
        # self.ui.stack.setCurrentWidget(self.ui.page_security)
    
    def update_sidebar_buttons(self):
        current = self.ui.stack.currentWidget()
        if current == self.ui.page_about:
            self.ui.btn_about.setStyleSheet(Styles.blue_button_outlined)
            self.ui.btn_security.setStyleSheet(Styles.blue_button)
            self.ui.btn_general.setStyleSheet(Styles.blue_button)
            self.ui.btn_import.setStyleSheet(Styles.blue_button)
            self.ui.btn_export.setStyleSheet(Styles.blue_button)
        elif current == self.ui.page_general:
            self.ui.btn_general.setStyleSheet(Styles.blue_button_outlined)
            self.ui.btn_about.setStyleSheet(Styles.blue_button)
            self.ui.btn_security.setStyleSheet(Styles.blue_button)
            self.ui.btn_import.setStyleSheet(Styles.blue_button)
            self.ui.btn_export.setStyleSheet(Styles.blue_button)
        elif current == self.ui.page_security:
            self.ui.btn_security.setStyleSheet(Styles.blue_button_outlined)
            self.ui.btn_general.setStyleSheet(Styles.blue_button)
            self.ui.btn_about.setStyleSheet(Styles.blue_button)
            self.ui.btn_import.setStyleSheet(Styles.blue_button)
            self.ui.btn_export.setStyleSheet(Styles.blue_button)
        elif current == self.ui.page_import:
            self.ui.btn_import.setStyleSheet(Styles.blue_button_outlined)
            self.ui.btn_security.setStyleSheet(Styles.blue_button)
            self.ui.btn_general.setStyleSheet(Styles.blue_button)
            self.ui.btn_about.setStyleSheet(Styles.blue_button)
            self.ui.btn_export.setStyleSheet(Styles.blue_button)
        elif current == self.ui.page_export:
            self.ui.btn_export.setStyleSheet(Styles.blue_button_outlined)
            self.ui.btn_import.setStyleSheet(Styles.blue_button)
            self.ui.btn_security.setStyleSheet(Styles.blue_button)
            self.ui.btn_general.setStyleSheet(Styles.blue_button)
            self.ui.btn_about.setStyleSheet(Styles.blue_button)
    
    def apply_styles(self):
        childs = self.ui.sidebar.children()
        for child in childs:
            # Skip non-widget children (Layouts usw.)
            if not hasattr(child, "setStyleSheet"):
                continue
            if isinstance(child, QPushButton):
                child.setStyleSheet(Styles.blue_button)
        self.ui.btn_general.setStyleSheet(Styles.blue_button_outlined)
        self.ui.btnCreateBackup.setStyleSheet(Styles.green_button_outlined)
        self.ui.btnRestoreBackup.setStyleSheet(Styles.yellow_button_outlined)
        self.ui.btnDeleteBackup.setStyleSheet(Styles.red_button_outlined)
        self.ui.btnClearBackup.setStyleSheet(Styles.red_button)
        utils.colorize_icon(self.ui.btnCreateBackup, "add", "green")
        utils.colorize_icon(self.ui.btnRestoreBackup, "reset", "yellow")
        utils.colorize_icon(self.ui.btnDeleteBackup, "trash", "red")
        utils.colorize_icon(self.ui.btnClearBackup, "trash", "dark")
        
        self.ui.btnEditCategory.setStyleSheet(Styles.yellow_button_outlined)
        self.ui.btnCreateCategory.setStyleSheet(Styles.green_button_outlined)
        self.ui.btnDeleteCategory.setStyleSheet(Styles.red_button_outlined)
        self.ui.btnCategpryColor.setStyleSheet(Styles.yellow_button_outlined)
        utils.colorize_icon(self.ui.btnEditCategory, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnCreateCategory, "add", "green")
        utils.colorize_icon(self.ui.btnDeleteCategory, "trash", "red")
        utils.colorize_icon(self.ui.btnCategpryColor, "eyedropper", "yellow")
        
        self.ui.btnSetBackupPath.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btnSetBackupPath, "check", "green")        
        self.ui.btnClearBackupPathLineEdit.setStyleSheet(Styles.red_button_outlined)
        utils.colorize_icon(self.ui.btnClearBackupPathLineEdit, "close", "red")
        self.ui.btnGetBackupPath.setStyleSheet(Styles.yellow_button_outlined)
        utils.colorize_icon(self.ui.btnGetBackupPath, "open", "yellow")
        self.ui.btn_apply_pw.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btn_apply_pw, "check", "green")        
        self.ui.btnSelectPath.setStyleSheet(Styles.yellow_button_outlined)
        utils.colorize_icon(self.ui.btnSelectPath, "open", "yellow")        
        self.ui.btnStartImport.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btnStartImport, "import", "green")
        self.ui.btnCheckUpdate.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btnCheckUpdate, "check_update", "green")
        self.ui.btnStartUpdate.setStyleSheet(Styles.green_button)
        utils.colorize_icon(self.ui.btnStartUpdate, "check", "dark")

        
    def _update_pw_strength(self):
        pw = self.ui.new_pw1.text()
        level = evaluate_password_strength(pw)
        self.strength_indicator.set_strength(level)
    
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
        self.ui.backupPathLineEdit.setText(settings.get("backup_path"))
        self.ui.autoUpdatesSelect.setChecked(settings.get("check_update"))
        self.ui.autoUpdatesSelect.toggled.connect(self._toggle_auto_check_update)
        self.ui.backupModeBox.currentIndexChanged.connect(self.update_backup_mode)
        self.ui.btnGetBackupPath.clicked.connect(self._get_backup_dir_path)
        self.ui.btnSetBackupPath.clicked.connect(self.set_backup_path)
        self.ui.btnClearBackupPathLineEdit.clicked.connect(self.ui.backupPathLineEdit.clear)
        self.ui.btnCheckUpdate.clicked.connect(self._check_updates)
        self.ui.btnStartUpdate.hide()
        self.update_general_page()
    
    def _load_all_backups(self):
        self.ui.backupDeleteBox.clear()        
        backups = self.db.get_all_backups()
        if not backups or len(backups) == 0:
            return
        self.ui.backupDeleteBox.addItems(backups)        
    
    def update_backup_mode(self, index):
        mode = self.mapping[index]
        settings = load_settings()
        settings["auto_backup"] = mode
        save_settings(settings)
        DialogPopup("Backup Information", f"Automatic backups set to: '{mode}'!", PopupType.INFO, self).exec()        
        
    def update_general_page(self):
        lates_backup = self.db.get_latest_backup()
        self._load_all_backups()
        if lates_backup:
            self.ui.btnDeleteBackup.setVisible(True)
            self.ui.btnRestoreBackup.setVisible(True)
            settings = load_settings()
            last_backup_raw = settings.get("last_backup")
            last_backup_time = format_last_backup(last_backup_raw)
            self.ui.lastBackupLabel.setText(f"{last_backup_time}")
            self.ui.btnClearBackup.show()
            self.ui.backupDeleteBox.show()
            self.ui.backupDeleteFrame.show()
        else:
            self.ui.backupDeleteBox.hide()
            self.ui.backupDeleteFrame.hide()
            self.ui.btnDeleteBackup.setVisible(False)
            self.ui.btnRestoreBackup.setVisible(False)
            self.ui.btnClearBackup.hide()
            self.ui.lastBackupLabel.setText("No Backups found!")            
            
    def create_new_backup(self):
        now = datetime.now()
        settings = load_settings()        
        self.db.create_backup()
        settings["last_backup"] = now.isoformat()
        save_settings(settings) 
        latest_backup = self.db.get_latest_backup()
        
        if not latest_backup:
            DialogPopup("Create Error", f"Cant find any backup!", PopupType.ERROR, self).exec()
            return
        self.update_general_page()
        DialogPopup("Create Success", f"Backup:\n{latest_backup}\n created successfully!", PopupType.SUCCESS, self).exec()        

    def restore_backup(self):
        latest_backup = self.db.get_latest_backup()
        if not latest_backup:
            DialogPopup("Restore Error", f"Cant find any backup!", PopupType.ERROR, self).exec()
            return
        confirm = QMessageBox.question(self, "Confirm Restore", "Are you sure you want to restore the backup?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:  
            self.db.apply_backup(latest_backup)
            self.db.reload_after_backup(self.ask_master_password)
            self.backup_restored.emit(self.db)
            DialogPopup("Restore Success", f"Backup:\n{latest_backup}\n restored successfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Restore Error", f"Failed to restore backup({latest_backup}):\n{e}", PopupType.ERROR, self).exec()    
        
    def delete_backup(self):
        delete_backup = self.ui.backupDeleteBox.currentText()
        if not delete_backup:
            return
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this backup?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:        
            self.db.delete_backup(delete_backup)
            self.update_general_page()
            DialogPopup("Delete Success", f"Backup:\n{delete_backup}\n deleted successfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Delete Error", f"Failed to delete backup:\n{e}", PopupType.ERROR, self).exec()    

    def clear_backups(self):
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this backup?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:
            removed = self.db.clear_backups()
            self.update_general_page()
            DialogPopup("Clear Success", f"Removed {removed}x backups deleted successfully", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Clear Error", f"Failed to clear backups:\n{e}", PopupType.ERROR, self).exec()    

    def set_backup_path(self):
        new_path = self.ui.backupPathLineEdit.text()
        if not new_path:
            DialogPopup("Backup Error", f"No backup path found. Please enter a path and try again!", PopupType.ERROR, self).exec()    
            return
        try:
            settings = load_settings()
            new_path = os.path.abspath(new_path)
            old_path = os.path.abspath(settings.get("backup_path"))
            # print(f"Paths\nOld: {old_path}\nNew: {new_path}")
            if old_path == new_path:
                return
            
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                
            settings["backup_path"] = str(new_path)
            save_settings(settings)
            self.db.create_backup()
            self.update_general_page()
            DialogPopup("Backup Success", f"Backuppath changed to:\n'{new_path}' successfully!\nNew Backup created!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Backup Error", f"Failed to edit backuppath:\n{e}", PopupType.ERROR, self).exec()   

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
        self.ui.btn_import.clicked.connect(
            lambda: self.ui.stack.setCurrentWidget(self.ui.page_import)
        )
        self.ui.btn_export.clicked.connect(
            lambda: self.ui.stack.setCurrentWidget(self.ui.page_export)
        )
    
    def apply_master_pw(self):
        old = self.ui.old_pw.text().strip()
        new1 = self.ui.new_pw1.text().strip()
        new2 = self.ui.new_pw2.text().strip()

        if new1 != new2:
            DialogPopup("Edit Error", "New passwords do not match!", PopupType.ERROR, self).exec()
            return

        if len(new1) <= 6:
            DialogPopup("Edit Error", "Password need min. 6 characters!", PopupType.ERROR, self).exec()
            return

        # Check old password
        if not self.db.unlock_vault(old):
            DialogPopup("Edit Error", "Old master password incorrect!", PopupType.ERROR, self).exec()
            return

        try:
            self.db.change_master_password(old, new1)
            self.ui.old_pw.clear()
            self.ui.new_pw1.clear()
            self.ui.new_pw2.clear()
            DialogPopup("Edit Success", f"Master Password successfully changed!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Error", f"Failed to change master password:\n{e}", PopupType.ERROR, self).exec()    

    def toggle_masterpw_visibility(self, checked: bool):
        mode = QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        self.ui.new_pw1.setEchoMode(mode)
        self.ui.new_pw2.setEchoMode(mode)
        self.ui.old_pw.setEchoMode(mode)
            
    def setup_about_page(self):
        self.ui.aboutLabel.setText(TextStorage.ABOUT_TEXT)
    
    
    # Edit & Create category
    def setup_edit_category(self):
        self.ui.btnCategpryColor.clicked.connect(self.show_color_dialog)
        self.ui.btnCreateCategory.clicked.connect(self.create_category)
        self.ui.btnDeleteCategory.clicked.connect(self.delete_category)
        self.ui.btnEditCategory.clicked.connect(self.edit_category)
        self.update_edit_category()

    def update_edit_category(self):
        settings = load_settings()
        self.ui.editCategoryBox.clear()
        self.ui.editCategoryBox.addItems(settings.get("entry_categories"))
        self.ui.editCategoryBox.setCurrentText("")

    def create_category(self):
        settings = load_settings()
        categories: list = settings["entry_categories"]
        cat_name = self.ui.categoryCreatLineEdit.text().strip().capitalize()
        if not cat_name:
            DialogPopup("Create Warning", "Please enter a categoryname!", PopupType.WARNING, self).exec()
            return
        
        if cat_name in categories:
            DialogPopup("Create Warning", f"Category with name {cat_name} already exists!", PopupType.WARNING, self).exec()
            return
        
        categories.append(cat_name)
        settings["entry_categories"] = categories
        
        if not self.new_category_color:
            DialogPopup("Create Warning", "No new category color selected!", PopupType.WARNING, self).exec()
            return
        r, g, b, a = self.new_category_color.getRgb()
        color_string = f"rgba({r}, {g}, {b}, {a})"
        try:                
            colors = settings["category_colors"]
            colors[f"{cat_name}"] = color_string
            settings["category_colors"] = colors
            save_settings(settings)
            self.ui.categoryCreatLineEdit.clear()
            self.new_category_color = None
            self.ui.btnCategpryColor.setStyleSheet(
                f"background-color: #2d2d30;"
                f"color: white;"
            )
            self.update_edit_category()
            DialogPopup("Create Success", f"New category:\n'{cat_name}'\nsuccessfully created!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Create Error",  f"Cant create category '{cat_name}':\n{e}", PopupType.ERROR, self).exec()    
        
    def delete_category(self):
        settings = load_settings()
        user_categories: list = settings.get("entry_categories")
        cat_colors: dict = settings.get("category_colors")
        cat = self.ui.editCategoryBox.currentText()
        if not cat:
            DialogPopup("Delete Warning", f"No category selected!", PopupType.WARNING, self).exec()
            return
        
        if cat not in user_categories:
            DialogPopup("Delete Warning", f"Category '{cat}' didnt exists!", PopupType.WARNING, self).exec()
            return
        
        if not cat_colors[cat]:
            DialogPopup("Delete Warning", f"Color for category '{cat}' didnt exists!", PopupType.WARNING, self).exec()
            return
        try:
            user_categories.remove(cat)
            del cat_colors[cat]            
            change_entrys = self.db.get_entries_by_category(cat)
            for entry in change_entrys:
                entry_id, service, username, category = entry
                self.db.edit_category(entry_id=int(entry_id), new_category="General")
            settings["entry_categories"] = user_categories
            settings["category_colors"] = cat_colors
            save_settings(settings)
            self.update_edit_category()
            self.category_deleted.emit()
            DialogPopup("Delete Success", f"Category:\n{cat}'\nsuccessfully removed!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Delete Error", f"Cant remove category '{cat}':\n{e}", PopupType.ERROR, self).exec()    
        
    def edit_category(self):
        cat = self.ui.editCategoryBox.currentText()
        if not cat:
            DialogPopup("Edit Warning", f"No category selected!", PopupType.WARNING, self).exec()
            return
        try:
            settings = load_settings()
            user_categories: list = settings.get("entry_categories")
            cat_colors: dict = settings.get("category_colors")
            
            if not cat in user_categories:
                DialogPopup("Edit Error", f"Category '{cat}' didnt exists!", PopupType.ERROR, self).exec() 
                return
            
            old_name = cat
            last_name = cat
            old_color = cat_colors.get(cat)

            dialog = CategoryEditDialog(old_name, old_color, self)
            if dialog.exec() != QDialog.DialogCode.Accepted:
                return
            
            new_name, new_color = dialog.get_results()
            if new_name == old_name and new_color == old_color:
                return
            
            if new_name != old_name:
                if new_name in user_categories:
                    DialogPopup("Edit Error", "Category name already exists!", PopupType.ERROR, self).exec()        
                    return
                
                index = user_categories.index(old_name)
                user_categories[index] = new_name
                cat_colors[new_name] = cat_colors.get(old_name, "rgba(211, 211, 211, 140)")
                del cat_colors[old_name]
                entries_to_change = self.db.get_entries_by_category(old_name)
                if len(entries_to_change) >= 0:
                    for entry in entries_to_change:
                        entry_id, service, username, password, category = entry
                        self.db.edit_category(int(entry_id), new_name)
                old_name = new_name
            
            if new_color != old_color:
                cat_colors[old_name] = new_color
            
            settings["entry_categories"] = user_categories
            settings["category_colors"] = cat_colors
            save_settings(settings)
            self.category_updated.emit()
            self.update_general_page()
            self.ui.editCategoryBox.setCurrentIndex(-1)
            DialogPopup("Edit Success",  f"Category\n'{last_name}'\nupdated to\n'{new_name}'\n successfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Edit Error", f"Cant edit category '{cat}':\n{e}", PopupType.ERROR, self).exec()    

    def show_color_dialog(self):        
        dialog = QColorDialog(QColor(211, 211, 211, 140))
        dialog.setOptions(QColorDialog.ColorDialogOption.ShowAlphaChannel | 
                          QColorDialog.ColorDialogOption.DontUseNativeDialog)
        
        if dialog.exec() == QColorDialog.DialogCode.Accepted:
            selected_color = dialog.selectedColor()
            self.current_color = selected_color 
            self.new_category_color = selected_color
            r, g, b, a = selected_color.getRgb()            
            self.ui.btnPreviewCatColor.setStyleSheet(
                "QPushButton:disabled{"
                f"background-color: {selected_color.name()};"
                f"color: white;" 
                "}"
            )
        else:
            return
        
    # Import
    def setup_import_page(self):
        import_modes = ["Firefox", "Chrome", "PassTreasure"]
        self.ui.importModeBox.addItems(import_modes)
        self.ui.progressFrame.hide()
    
    def get_import_path(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", filter="*.csv")
        if not file_path:
            return
        self.ui.importFilePathLineEdit.setText(file_path)
    
    def start_import(self):
        mode = self.ui.importModeBox.currentText().lower()
        if not mode:
            DialogPopup("Import Warning", f"Missing importmode. No importmode selected!\nPlease select a importmode!.", PopupType.WARNING, self).exec()        
            return
        file_path = self.ui.importFilePathLineEdit.text().strip()
        if not file_path:
            DialogPopup("Import Warning", "Missing import filepath. No filepath set!\nPlease enter a filepath to import from.", PopupType.WARNING, self).exec()        
            return
        pw = self.ask_master_password()
        if not pw:
            return
        
        from PySide6.QtCore import QThread
        
        self.qthread = QThread()
        self.worker = CsvImportWorker(VAULT_PATH, file_path, pw, mode)
        self.worker.moveToThread(self.qthread)
        
        self.worker.progress.connect(self.on_import_progress)
        self.worker.finished.connect(self.on_import_finished)
        self.worker.error.connect(self.on_import_error)
        
        self.qthread.started.connect(self.worker.run)
        self.qthread.start() 
        
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.clear()
        self.ui.progressFrame.show()
        
    def on_import_progress(self, count, total):
        percentage = int(count / total * 100)
        self.ui.progressLabel.setText(f"Importing {count} / {total} entries...")
        self.ui.progressBar.setValue(percentage)

    def on_import_finished(self):
        self.ui.progressBar.setValue(100)
        self.ui.progressLabel.setText("Import finished!")
        self.qthread.quit()
        self.qthread.wait()
        DialogPopup("Import Success", f"Import finished!", PopupType.SUCCESS, self).exec()        
        self.import_successfully.emit()
        QTimer.singleShot(1000, self.reset_import_ui)

    def on_import_error(self, err):
        DialogPopup("Import Error", f"Error at import:\n{err}", PopupType.ERROR, self).exec()
        self.qthread.quit()
        self.qthread.wait()

    def reset_import_ui(self):
        self.ui.importFilePathLineEdit.clear()
        self.ui.importModeBox.setCurrentIndex(-1)
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.clear()
        self.ui.progressFrame.hide()
        
    # autologout
    def toggle_autologout(self, checked: bool):
        settings = load_settings()
        if checked:
            self.autologout_activated.emit()
            # logout_ms = settings.get("auto_logouttime")
            # print(f"Autologout started with {logout_ms} ms!")
        else:
            self.autologout_deactivated.emit()
            # print(f"Autologout stopped!")
        settings["auto_logout"] = checked
        save_settings(settings)
        
    def set_autologout_time(self):
        settings = load_settings()
        ms = settings.get("auto_logouttime")
        minutes = ms // 60000
        ms %= 60000
        seconds = ms // 1000
        t = QTime(0, minutes, seconds)
        self.ui.autoLogoutTimeEdit.setTime(t)
        self.ui.autoLogoutCheckBox.setChecked(settings.get("auto_logout"))
    
    def get_autologout_time(self):
        time_value = self.ui.autoLogoutTimeEdit.time()
        logout_ms = (
            time_value.minute() * 60 * 1000
            + time_value.second() * 1000
        )
        # print(f"Logouttime: {time_value.minute()}:{time_value.second()}\nin ms: {logout_ms}")
        settings = load_settings()
        settings["auto_logouttime"] = logout_ms       
        save_settings(settings)

    def toggle_auto_hide_details(self, checked: bool):
        settings = load_settings()
        settings["auto_hide_details"] = checked
        save_settings(settings)

    def set_auto_hide_details_time(self):
        settings = load_settings()
        ms = settings.get("auto_hide_details_time")
        minutes = ms // 60000
        ms %= 60000
        seconds = ms // 1000
        t = QTime(0, minutes, seconds)
        self.ui.autoHideDetailsTimeEdit.setTime(t)
        self.ui.autoHideDetailsCheckBox.setChecked(settings.get("auto_hide_details"))
        
    def get_auto_hide_details_time(self):
        settings = load_settings()
        time_value = self.ui.autoHideDetailsTimeEdit.time()
        hide_ms = (
            time_value.minute() * 60 * 1000
            + time_value.second() * 1000
        )
        settings["auto_hide_details_time"] = hide_ms
        save_settings(settings)
    
    
    # export    
    def setup_export_page(self):
        self.ui.btnStartExport.setStyleSheet(Styles.green_button_outlined)
        self.ui.btnExportPath.setStyleSheet(Styles.yellow_button_outlined)
        utils.colorize_icon(self.ui.btnExportPath, "open", "yellow")
        utils.colorize_icon(self.ui.btnStartExport, "export", "green")
        self.ui.btnExportPath.clicked.connect(self._get_export_file_path)
        self.ui.btnStartExport.clicked.connect(self.start_export)
        self.ui.fileEndingBox.addItems(EXPORT_TYPES)
    
    def start_export(self):
        filename = self.ui.exportFilenameLineEdit.text()
        if not filename:
            filename = self.default_export_name

        file_type = self.ui.fileEndingBox.currentText()
        if not file_type:
            DialogPopup("Export Error", f"No filetype selected! Please select a filetype and try again!", PopupType.ERROR, self).exec()        
            return
        
        filename += file_type
                
        dir_path = self.ui.exportFileLineEdit.text()
        if not dir_path:
            DialogPopup("Export Error", f"No directory found! Please select a directory to export.", PopupType.ERROR, self).exec()        
            return
        file_path = os.path.join(os.path.abspath(dir_path), filename)
        try:
            entries = self.db.get_export_entries()
            export_entries = []
            field_names = ["id", "service", "username", "password", "category", "url", "note"]
            for entry in entries:
                export_entry = {}
                entry_id, service, username, category, url, note = entry
                export_entry["id"] = entry_id            
                export_entry["service"] = service
                export_entry["username"] = username
                export_entry["category"] = category
                export_entry["url"] = url
                export_entry["note"] = note            
                
                password = self.db.get_password(entry_id)
                if password:
                    export_entry["password"] = password
                
                export_entries.append(export_entry)
            if len(export_entries) == 0:
                DialogPopup("Export Information", "No entries to export found.", PopupType.INFO, self).exec()
                return
            
            if file_type == ".csv":
                with open(file_path, mode="w", newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(export_entries)
            elif file_type == ".json":
                with open(file_path, mode="w") as file:
                    data = json.dumps(export_entries, indent=4)
                    file.write(data)
        
            self.ui.fileEndingBox.setCurrentIndex(-1)
            self.ui.exportFilenameLineEdit.clear()
            self.ui.exportFileLineEdit.clear()
            DialogPopup("Export Success", f"Exporting {len(export_entries)}x entries to:\n'{filename}'\nsuccessfully!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Export Error", f"Failure at export to csv:\n{e}", PopupType.ERROR, self).exec()        
    
    def _get_export_file_path(self):
        file_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select directory."
        )        
        if not file_path:
            return
        self.ui.exportFileLineEdit.setText(file_path)
    
    def _get_backup_dir_path(self):
        file_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select directory."
        )        
        if not file_path:
            return
        self.ui.backupPathLineEdit.setText(file_path)        

    def _reset_update_status(self):
        self.ui.updateStatusLabel.setText("Check not started.")
        self.ui.updateStatusLabel.setStyleSheet("color: #fff;")

    def _on_btnStartUpdate_click(self, url: str):
        self._reset_update_status()
        self.ui.btnStartUpdate.hide()

        utils.open_url(url)
    
    
    def _toggle_auto_check_update(self, checked: bool):
        settings = load_settings()
        settings["check_update"] = checked
        save_settings(settings)
    
    def _check_updates(self):
        try:
            update_result = utils.check_for_update()
            if not update_result.get("update_available"):
                self.ui.updateStatusLabel.setText("Currently no updates available.")
                self.ui.updateStatusLabel.setStyleSheet(f"color: {Styles.COLORS['red']};")
                return QTimer.singleShot(5000, self._reset_update_status)
            self.ui.updateStatusLabel.setText(f"Update {update_result['version']} available.")
            self.ui.updateStatusLabel.setStyleSheet(f"color: {Styles.COLORS['green']};")
            self.ui.btnStartUpdate.show()
            self.ui.btnStartUpdate.clicked.connect(lambda: self._on_btnStartUpdate_click(update_result["download_url"]))
        except Exception as e:
            DialogPopup("Update Error", f"Failed checking for updates:\n{e}", PopupType.ERROR, self).exec()  