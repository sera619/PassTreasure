from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog, QLineEdit, QColorDialog, QPushButton, QVBoxLayout, QFileDialog
from src.settingswindow_ui import Ui_SettingsWindow
import resources_rc
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt, Signal, QTimer, QTime
from datetime import datetime
from gui.category_edit_dialog import CategoryEditDialog
from gui.password_strength_indicator import PasswordStrengthIndicator
from backend.import_worker import CsvImportWorker
from backend.password_strength_logic import evaluate_password_strength
from config import ABOUT_TEXT, load_settings, save_settings, format_last_backup, Styles, VAULT_PATH, resource_path
from backend.database import PasswordDatabase
import utils
import os, csv


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
        
        self.ui.btn_apply_pw.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btn_apply_pw, "check", "green")
        
        self.ui.btnSelectPath.setStyleSheet(Styles.yellow_button_outlined)
        utils.colorize_icon(self.ui.btnSelectPath, "open", "yellow")
        
        self.ui.btnStartImport.setStyleSheet(Styles.green_button_outlined)
        utils.colorize_icon(self.ui.btnStartImport, "import", "green")
        
    
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
        if confirm != QMessageBox.StandardButton.Yes:
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
            if confirm != QMessageBox.StandardButton.Yes:
                return
            try:        
                self.db.delete_backup(latest_backup)
                self.update_general_page()
                QMessageBox.information(self, "Success", f"Backup:\n{latest_backup}\n deleted successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete backup:\n{e}")
    
    def clear_backups(self):
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this backup?")
        if confirm != QMessageBox.StandardButton.Yes:
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
            QMessageBox.warning(self, "Error", "New passwords do not match!")
            return

        if len(new1) <= 6:
            QMessageBox.warning(self, "Error", "Password need min. 6 characters!")
            return

        # Check old password
        if not self.db.unlock_vault(old):
            QMessageBox.warning(self, "Error", "Old password incorrect!")
            return

        try:
            self.db.change_master_password(old, new1)
            self.ui.old_pw.clear()
            self.ui.new_pw1.clear()
            self.ui.new_pw2.clear()
            
            QMessageBox.information(self, "Success", "Master password updated!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def toggle_masterpw_visibility(self, checked: bool):
        mode = QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        self.ui.new_pw1.setEchoMode(mode)
        self.ui.new_pw2.setEchoMode(mode)
        self.ui.old_pw.setEchoMode(mode)
            
    def setup_about_page(self):
        self.ui.aboutLabel.setText(ABOUT_TEXT)
    
    
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
            QMessageBox.warning(self, "Warning", f"Please enter a category name!")
            return
        
        if cat_name in categories:
            QMessageBox.warning(self, "Warning", f"Category with name {cat_name} already exists!")
            return
        
        categories.append(cat_name)
        settings["entry_categories"] = categories
        
        if not self.new_category_color:
            QMessageBox.warning(self, "Warning", "No new category color selected!")
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
            QMessageBox.information(self, "Success", f"New category:\n'{cat_name}'\nsuccessfully created!")
        except Exception as e:
            QMessageBox.critical(self, "Error!", f"Cant create category '{cat_name}':\n{e}")
           
    def delete_category(self):
        settings = load_settings()
        user_categories: list = settings.get("entry_categories")
        cat_colors: dict = settings.get("category_colors")
        cat = self.ui.editCategoryBox.currentText()
        if not cat:
            QMessageBox.warning(self, "Error", f"No category selected!")
            return
        
        if cat not in user_categories:
            QMessageBox.warning(self, "Error", f"Category '{cat}' didnt exists!")
            return
        
        if not cat_colors[cat]:
            QMessageBox.warning(self, "Error", f"Color for category '{cat}' didnt exists!")
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
            QMessageBox.information(self, "Success", f"Category:\n{cat}'\nsuccessfully removed!")
        except Exception as e:
            QMessageBox.critical(self, "Error!", f"Cant remove category '{cat}':\n{e}")
        
    def edit_category(self):
        cat = self.ui.editCategoryBox.currentText()
        if not cat:
            QMessageBox.warning(self, "Error", f"No category selected!")
            return
        try:
            settings = load_settings()
            user_categories: list = settings.get("entry_categories")
            cat_colors: dict = settings.get("category_colors")
            
            if not cat in user_categories:
                QMessageBox.warning(self, "Error", f"Category '{cat}' didnt exists!")
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
                    QMessageBox.warning(self, "Error", "Category name already exists!")
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
            QMessageBox.information(self, "Success", f"Category\n'{last_name}'\nupdated!")
        except Exception as e:
            QMessageBox.critical(self, "Error!", f"Cant edit category '{cat}':\n{e}")
           
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
        browsers = ["Firefox", "Chrome", "Opera"]
        self.ui.browserBox.addItems(browsers)
        self.ui.progressFrame.hide()
    
    def get_import_path(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", filter="*.csv")
        if not file_path:
            return
        self.ui.importFilePathLineEdit.setText(file_path)
    
    def start_import(self):
        mode = self.ui.browserBox.currentText().lower()
        if not mode:
            QMessageBox.warning(self, "Missing Import Mode", "No import mode selected!\nPlease select a browser.")
            return
        file_path = self.ui.importFilePathLineEdit.text().strip()
        if not file_path:
            QMessageBox.warning(self, "Missing File Path", "No filepath found! Please enter a path.")
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
        QMessageBox.information(self, "Import", "Import finished!")
        self.import_successfully.emit()
        QTimer.singleShot(1000, self.reset_import_ui)

    def on_import_error(self, err):
        QMessageBox.critical(self, "Error at import", err)
        self.qthread.quit()
        self.qthread.wait()

    def reset_import_ui(self):
        self.ui.importFilePathLineEdit.clear()
        self.ui.browserBox.setCurrentIndex(-1)
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
        self.ui.btnExportPath.clicked.connect(self._get_file_path)
        self.ui.btnStartExport.clicked.connect(self.start_export)
    
    def start_export(self):
        filename = self.ui.exportFilenameLineEdit.text()
        if not filename:
            filename = "FileTreasure-PasswordExport"
        filename = filename + ".csv"
        dir_path = self.ui.exportFileLineEdit.text()
        if not dir_path:
            QMessageBox.information(self, "No Directory", "Please select a directory to save.")
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
                QMessageBox.information(self, "No Entries", "No entries to export found.")
                return
            
            with open(file_path, mode="w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(export_entries)
            self.ui.exportFilenameLineEdit.clear()
            self.ui.exportFileLineEdit.clear()
            QMessageBox.information(self, "Export success", "Export successfully finished!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failure at export to csv:\n{e}")
    
    def _get_file_path(self):
        file_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select directory."
        )        
        if not file_path:
            return
        self.ui.exportFileLineEdit.setText(file_path)
