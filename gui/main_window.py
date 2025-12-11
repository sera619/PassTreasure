from PySide6.QtWidgets import (
    QApplication,QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget,
    QPushButton, QLineEdit, QInputDialog, QMessageBox, QTextEdit,QListWidgetItem, QToolTip, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer, Signal, QPropertyAnimation, QEasingCurve
from src.mainwindow_ui import Ui_MainWindow
from gui.change_password_popup import ChangePasswordPopup
from gui.settings_window import SettingsWindow
from gui.category_popup import CategoryPopup
from gui.vault_listiem import VaultListItemWidget
from gui.new_entry_dialog import NewEntryDialog
from gui.edit_url_dialog import EditURLDialog
from gui.edit_note_dialog import EditNoteDialog
from gui.dialog_popup import DialogPopup
from gui.get_text_dialog_popup import GetTextDialogPopup
from gui.password_strength_indicator import PasswordStrengthIndicator

from backend.password_strength_logic import evaluate_password_strength
from backend.database import PasswordDatabase
from backend.inactivity_watcher import AutoLocker, InactivityWatcher

from config import VERSION_NUM, Styles, IS_DEBUGGING, PopupType
from datetime import datetime
from utils import load_settings, save_settings
import utils

class MainWindow(QWidget):
    logout_success = Signal()
    auto_logout_success = Signal()
    def __init__(self, db: PasswordDatabase):
        super().__init__()
        self.db = db  # unlocked PasswordDatabase instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PassTreasure - Vault")
        self.entry_cache = []
        self.watcher = None
        self.autolock = None
        self.settings_window = None
        self.apply_dark_theme()
        self.build_ui()  
        self.apply_styles()
        self.strength_indicator = PasswordStrengthIndicator(self)
        self.ui.indicatorHolder.addWidget(self.strength_indicator)  

        if IS_DEBUGGING:
            loaded_entries = self.db.get_all_entries()
            if len(loaded_entries) == 0:
                self.db.add_test_entries()

        self.details_open = False
        self.details_max_width = 377
        self.ui.detailFrame.setMaximumWidth(0)
        self.ui.detailFrame.hide()
        self.ui.btnDelete.hide()
        
        self._block_click = False
        self.load_entries()
        self.check_auto_backup()
        self.check_autologout()
        QTimer.singleShot(0, self.clear_initial_selection)
            
    # autologout
    def start_autologout(self):
        settings = load_settings()
        self.watcher = InactivityWatcher()
        self.autolock = AutoLocker(settings.get("auto_logouttime"), self.auto_logout)
        QApplication.instance().installEventFilter(self.watcher)
        self.watcher.user_active.connect(self.autolock.reset)
    
    def stop_autologout(self):
        if not hasattr(self, "watcher") or self.watcher is None:
            return False
        QApplication.instance().removeEventFilter(self.watcher)        
        if hasattr(self, "autolock") or self.autolock is not None:
            self.autolock.timer.stop()        
        self.watcher = None
        self.autolock = None
        return True
        
    def check_autologout(self):
        settings = load_settings()
        if not settings.get("auto_logout"):
            return
        # timeout_ms = settings.get("auto_logouttime")
        # print(f"Start: Autologout started with {timeout_ms} ms!")
        self.start_autologout()
 
    # Dark Theme
    def apply_dark_theme(self):
        self.setStyleSheet(Styles.dark_style)

    def apply_styles(self):
        self.ui.btnSettings.setStyleSheet(Styles.yellow_button_outlined)
        self.ui.btnLogout.setStyleSheet(Styles.red_button_outlined)
        self.ui.btnAdd.setStyleSheet(Styles.green_button)
        self.ui.btnDelete.setStyleSheet(Styles.red_button_outlined)
        utils.colorize_icon(self.ui.btnSettings, "settings", "yellow")
        utils.colorize_icon(self.ui.btnLogout, "exit", "red")
        utils.colorize_icon(self.ui.btnAdd, "add", "dark")
        utils.colorize_icon(self.ui.btnDelete, "trash", "red")

        self.ui.btnEditCategory.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditPass.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditService.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditUsername.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditUrl.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditNote.setStyleSheet(Styles.yellow_button_outlined_low)
        utils.colorize_icon(self.ui.btnEditCategory, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnEditPass, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnEditService, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnEditUsername, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnEditUrl, "pencil", "yellow")
        utils.colorize_icon(self.ui.btnEditNote, "pencil", "yellow")
        
        self.ui.btnClearEntries.setStyleSheet(Styles.red_button_outlined)
        self.ui.btnCopyPass.setStyleSheet(Styles.dark_button_outlined)
        self.ui.btnShowPass.setStyleSheet(Styles.dark_button_outlined)
        self.ui.btnCloseDetails.setStyleSheet(Styles.red_button_outlined)
        utils.colorize_icon(self.ui.btnClearEntries, "trash", "red")
        utils.colorize_icon(self.ui.btnCopyPass, "copy", "dark")
        utils.colorize_icon(self.ui.btnShowPass, "show", "dark")
        utils.colorize_icon(self.ui.btnCloseDetails, "hiden", "red")
        self.ui.listWidget.setStyleSheet(Styles.list_widget_style)
    
    def build_ui(self):
        pixmap = QPixmap(":/assets/icon.png")
        pixmap = pixmap.scaled(35, 35)
        self.ui.mainTitleIcon.setPixmap(pixmap)
        
        self.ui.listWidget.currentItemChanged.connect(self.update_details)
        self.ui.btnAdd.clicked.connect(self.add_entry)
        self.ui.btnDelete.clicked.connect(self.delete_entry)
        
        self.ui.btnEditUsername.clicked.connect(self.edit_entry_username)
        self.ui.btnEditService.clicked.connect(self.edit_entry_service)
        self.ui.btnEditPass.clicked.connect(self.edit_entry_password)
        self.ui.btnEditUrl.clicked.connect(self.edit_entry_url)
        self.ui.btnEditNote.clicked.connect(self.edit_entry_note)
        
        self.ui.btnShowPass.clicked.connect(self.toggle_password_visibility)
        self.ui.btnCopyPass.clicked.connect(self.copy_password_to_clipboard)
        self.ui.btnSettings.clicked.connect(self.open_settings)
        self.ui.btnEditCategory.clicked.connect(self.edit_entry_category)
        self.ui.searchLineEdit.textChanged.connect(self.filter_list)
        self.ui.btnCloseDetails.clicked.connect(self.close_details)
        self.ui.btnClearEntries.clicked.connect(self.clear_all_entries)
                
        self.ui.footerLabel.setText(f"PassTreasure v{VERSION_NUM} © S3R43o3 2025")
        self.ui.sortBox.addItems([
            "ID",
            "Service",
            "Username",
            "Category"
        ])        
        self.ui.sortBox.currentIndexChanged.connect(self.sort_by_selection)
        self.ui.mainLayout.setStretch(4, 3)
        self.ui.btnLogout.clicked.connect(self.logout)
    
    def clear_initial_selection(self):
        self.ui.listWidget.blockSignals(True)
        self.ui.listWidget.setCurrentRow(-1)
        self.ui.listWidget.clearSelection()
        self.hide_details()
        self.ui.listWidget.blockSignals(False)
    
    def show_details(self):
        self.ui.detailFrame.show()
        self.ui.btnDelete.show()
        self.ui.detailLabel.hide()
        if not self.details_open:
            self.toggle_details()
        
    def hide_details(self):
        if self.details_open:
            self.toggle_details()
        self.ui.btnDelete.hide()
        selected = self.ui.listWidget.currentItem()
        if selected:
            self.ui.listWidget.setCurrentRow(-1)

    def sort_list(self, role_key):
        self.entry_cache.sort(key= lambda e: e[role_key])
        self.render_list()
        
    def sort_by_selection(self):
        text = self.ui.sortBox.currentText()
        self.sort_list(text.lower())
    
    def auto_logout(self):
        if self.db.disconnect():
            self.close()     
            self.stop_autologout()
            if self.settings_window:
                self.settings_window.close()
                self.settings_window = None
            self.auto_logout_success.emit()
    
    def logout(self):
        if self.db.disconnect():
            self.close()     
            self.stop_autologout()
            if self.settings_window:
                self.settings_window.close()
                self.settings_window = None
            self.logout_success.emit()
        
    def render_list(self):
        lw = self.ui.listWidget
        lw.clear()

        for entry in self.entry_cache:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, entry["id"])
            item.setData(Qt.ItemDataRole.UserRole + 1, entry["service"])
            item.setData(Qt.ItemDataRole.UserRole + 2, entry["username"])
            item.setData(Qt.ItemDataRole.UserRole + 3, entry["category"])

            widget = VaultListItemWidget(
                entry["id"], entry["service"], entry["username"], entry["category"]
            )

            item.setSizeHint(widget.sizeHint())
            lw.addItem(item)
            lw.setItemWidget(item, widget)
            # -------------------------
    # Load / Refresh entries
    # -------------------------
    def load_entries(self):
        self.ui.listWidget.clear()
        try:
            entries = self.db.get_all_entries()
            self.entry_cache.clear()
            for entry in entries:
                entry_id, service, username, category = entry
                self.entry_cache.append({
                    "id": entry_id,
                    "service": service,
                    "username": username,
                    "category": category
                })
                # item_text = f"{entry_id}: {service}[{category}] ({username})"
                # item = QListWidgetItem(item_text)
                # item.setData(Qt.ItemDataRole.UserRole, category)
                # item.setBackground(category_colors.get(category, QColor(255, 255, 255)))
                widget = VaultListItemWidget(int(entry_id), service, username, category)
                item = QListWidgetItem()
                item.setData(Qt.ItemDataRole.UserRole, entry_id)
                item.setData(Qt.ItemDataRole.UserRole + 1, service)
                item.setData(Qt.ItemDataRole.UserRole + 2, username)
                item.setData(Qt.ItemDataRole.UserRole + 3, category)
                item.setSizeHint(widget.sizeHint())
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, widget)                
        except Exception as e:
            DialogPopup("Error", f"Failed to load entries:\n{e}", PopupType.ERROR, self).exec()    

    # -------------------------
    # Update detail view
    # -------------------------
    def close_details(self):
        self.hide_details()
        self.ui.listWidget.setCurrentItem(None)
      
    def update_details(self, current: QListWidgetItem, previous=None):
        if not current:
            self.hide_details()
            return
        #entry_id = int(current.text().split(":")[0])
        entry_id = current.data(Qt.ItemDataRole.UserRole)
        service = current.data(Qt.ItemDataRole.UserRole + 1)
        username = current.data(Qt.ItemDataRole.UserRole + 2)
        category = current.data(Qt.ItemDataRole.UserRole + 3)
        
        try:
            self.show_details()
            pw = self.db.get_password(entry_id)
            self._current_plain_password = pw
            self._password_visible = False
            details = self.db.get_entry_details(entry_id)
            level = evaluate_password_strength(pw)
            self.strength_indicator.set_strength(level)
            self.ui.serviceLabel.setText(service)
            self.ui.usernameLabel.setText(username)
            self.ui.passLabel.setText("•" * len(pw))
            
            settings = load_settings()
            colors = settings.get("category_colors")            
            self.ui.categoryLabel.setStyleSheet(f"""
                                           font: 700 8pt "Segoe UI"; 
                                           border-radius: 5px; 
                                           background: {colors[category]};
                                           """)
            self.ui.categoryLabel.setText(category)
            self.ui.urlLabel.setText(details.get("url"))
            self.ui.noteLabel.setText(details.get("note"))
            
            def format_datetime(dt_str):
                try:
                    dt = datetime.fromisoformat(dt_str)
                    return dt.strftime("%d.%m.%Y %H:%M")
                except Exception:
                    return "Unknown"            
            
            created = format_datetime(details.get("created_at", "Unkmown"))
            updated = format_datetime(details.get("updated_at", "Unknown"))

            self.ui.createdLabel.setText(f"{created}")
            self.ui.updatedLabel.setText(f"{updated}")
            
            self.ui.detailStatus.setText("")
            
            auto_hide_details: bool = settings.get("auto_hide_details")
            auto_hide_time: int = settings.get("auto_hide_details_time")
            if auto_hide_details:
                QTimer.singleShot(auto_hide_time, self.hide_details)
            
        except Exception as e:
            self.ui.detailStatus.setText(f"Error loading password:\n{e}")

    def toggle_password_visibility(self):
        if not hasattr(self, "_current_plain_password"):
            return
        if self._password_visible:
            self.ui.passLabel.setText("•" * len(self._current_plain_password))
            self.ui.btnShowPass.setText("Show Password")
            self._password_visible = False
        else:
            self.ui.passLabel.setText(self._current_plain_password)
            self.ui.btnShowPass.setText("Hide Password")
            self._password_visible = True            
            QTimer.singleShot(5000, self.toggle_password_visibility)
    # -------------------------
    # Actions
    # -------------------------
    def add_entry(self):        
        enty_dialog = NewEntryDialog(self)
        enty_dialog.exec()
        data = enty_dialog.get_entry_data()
        if not data:
            return
            
        username = data["username"]
        service = data["service"]
        url = data["url"]
        password = data["password"]
        category = data["category"]
        note = data["note"]

        if not password:
            import secrets, string
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(chars) for _ in range(16))

        try:
            self.db.add_entry(service.strip(), username.strip(), password, category, url, note)
            self.load_entries()
            DialogPopup("Add Success", f"New entry:\n\n'{service}\n\nsuccessfully created.'", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Error", f"Failed to add entry:\n{e}", PopupType.ERROR, self).exec()

    def delete_entry(self):
        selected = self.ui.listWidget.currentItem()
        if not selected:
            return
        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this entry?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:
            self.db.delete_entry(entry_id)
            self.load_entries()
            self.hide_details()
            DialogPopup("Edit Success", f"Entry with id: {entry_id} successfully deleted!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Error", f"Failed to delete entry:\n{e}", PopupType.ERROR, self).exec()    
         
    def clear_all_entries(self):
        confirm = QMessageBox.question(self, "Confirm Clear", "Are you sure you want delete ALL entries?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:
            self.db.clear_entries()
            self.load_entries()
            self.hide_details()
            DialogPopup("Clear Success", f"Entries successfully cleared!", PopupType.SUCCESS, self).exec()        
        except Exception as e:
            DialogPopup("Error", f"Failed to clear entries:\n{e}", PopupType.ERROR, self).exec()    
 
    def edit_entry_username(self):
        selected =  self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()
        if not selected:
            return
        
        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        service = selected.data(Qt.ItemDataRole.UserRole + 1)        
        dialog = GetTextDialogPopup("Edit Username", f"Please enter a new username for service:\n{service}.", "username", self)
        if dialog.exec():
            new_username = dialog.get_value()
            if not new_username.strip():
                return
            
            try:
                self.db.edit_username(entry_id, new_username.strip())
                self.load_entries()
                # self.ui.listWidget.setCurrentRow(self.ui.listWidget.count() - 1)
                self.update_details(selected)
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"Username successfully updated for:\n\n'{service}'", PopupType.SUCCESS, self).exec()        
            except Exception as e:
                DialogPopup("Error", f"Failed to update username:\n{e}", PopupType.ERROR, self).exec()    
    
    def edit_entry_password(self):
        selected = self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()

        if not selected:
            return
        service_name = self.ui.serviceLabel.text()
        entry_id = selected.data(Qt.ItemDataRole.UserRole)

        dialog = ChangePasswordPopup(self)
        if dialog.exec():
            new_password = dialog.get_password()
            if not new_password:
                QMessageBox.warning(self, "Error", "No password provided.")
                return
            
            try:
                self.db.edit_password(entry_id, new_password)
                self.update_details(selected)
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"Password successfully updated for:\n\n'{service_name}'", PopupType.SUCCESS, self).exec()        
            except Exception as e:
                DialogPopup("Error", f"Failed to update oassword:\n{e}", PopupType.ERROR, self).exec()    
    
    def edit_entry_category(self):
        selected = self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()
        if not selected:
            return

        service_name = self.ui.serviceLabel.text()
        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        current_category = self.ui.categoryLabel.text()
        settings = load_settings()
        categories = settings["entry_categories"]
        dialog = CategoryPopup(service_name=service_name, parent=self, current_category=current_category, categories=categories)
        if dialog.exec():
            new_category = dialog.selected_category
            if new_category == current_category:
                return
            try:
                self.db.edit_category(entry_id, new_category)
                self.update_details(selected)
                self.load_entries()
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"Category successfully updated for:\n\n'{service_name}'", PopupType.SUCCESS, self).exec()
            except Exception as e:
                DialogPopup("Error", f"Failed to update category:\n{e}", PopupType.ERROR, self).exec()        
    
    def edit_entry_service(self):
        selected = self.ui.listWidget.currentItem()
        index  = self.ui.listWidget.currentIndex()
        if not selected:
            return

        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        current_service = self.ui.serviceLabel.text()
        dialog = GetTextDialogPopup("Edit Service", f"Please enter a new servicename for service:\n{current_service}.", "service", self)
        if dialog.exec():
            new_service = dialog.get_value()
            if not new_service.strip():
                return
            try:
                self.db.edit_service(entry_id, new_service.strip())
                self.load_entries()
                self.update_details(self.ui.listWidget.currentItem())
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"Service successfully updated for:\n\n'{current_service}' => '{new_service}'", PopupType.SUCCESS, self).exec()
            except Exception as e:
                DialogPopup("Error", f"Failed to update service:\n{e}", PopupType.ERROR, self).exec()        
            
    def edit_entry_url(self):        
        selected = self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()
        if not selected:
            return

        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        current_service = self.ui.serviceLabel.text()
        current_url = self.ui.urlLabel.text()
        dialog = EditURLDialog(current_service, current_url, self)
        if dialog.exec():
            new_url = dialog.get_url()
            if not new_url:
                QMessageBox.warning(self, "Error", "No URL provided.")
                return
            try:
                self.db.edit_url(entry_id, new_url.strip())
                self.load_entries()
                self.update_details(self.ui.listWidget.currentItem())
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"URL successfully updated for:\n\n'{current_service}'", PopupType.SUCCESS, self).exec()        
            except Exception as e:
                DialogPopup("Error", f"Failed to update url:\n{e}", PopupType.ERROR, self).exec()        
    
    def edit_entry_note(self):
        selected = self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()
        if not selected:
            return

        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        details = self.db.get_entry_details(entry_id)
        old_note = details.get("note")
        current_service = self.ui.serviceLabel.text()
        dialog = EditNoteDialog(current_service, old_note, self)
        if dialog.exec():
            new_note = dialog.get_note()
            try:
                self.db.edit_note(entry_id, new_note.strip())
                self.load_entries()
                self.update_details(self.ui.listWidget.currentItem())
                self.ui.listWidget.setCurrentIndex(index)
                DialogPopup("Edit Success", f"Note successfully updated for:\n\n'{current_service}'", PopupType.SUCCESS, self).exec()
            except Exception as e:
                DialogPopup("Error", f"Failed to update note:\n{e}", PopupType.ERROR, self).exec()        
    
    def copy_password_to_clipboard(self):
        if not hasattr(self, "_current_plain_password"):
            self.show_toast("No password loaded!")
            return
        pw = self._current_plain_password
        clipboard = QApplication.clipboard()
        clipboard.setText(pw)
        original_text = self.ui.btnCopyPass.text()
        self.ui.btnCopyPass.setText("✔ Copied!")
        QTimer.singleShot(1000, lambda: self.ui.btnCopyPass.setText(original_text))

        self.show_toast("Password copied!", parent=self.ui.detailBtnFrame)
        def clear_clip():
            if clipboard.text() == pw:
                clipboard.clear()
        QTimer.singleShot(10000, clear_clip)
        
    def show_toast(self, message, parent):
        """
        A small non-blocking toast-like popup that fades out.
        """
        toast = QLabel(message, self)
        toast.setStyleSheet("""
            QLabel {
                background-color: #333;
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
            }
        """)
        toast.setWindowFlags(Qt.ToolTip)
        toast.setParent(parent)
        toast.adjustSize()
        # Position: bottom-right inside window
        px = parent.width() / 2 - toast.width() / 2
        py = parent.height() - toast.height() 

        toast.move(int(px), int(py))

        toast.show()

        # Hide after 2 seconds
        QTimer.singleShot(2000, toast.close)
    
    def open_settings(self):
        self.settings_window = SettingsWindow(self.db)
        self.settings_window.category_deleted.connect(self.load_entries)
        self.settings_window.backup_restored.connect(self.load_entries)
        self.settings_window.category_updated.connect(self.load_entries)
        self.settings_window.import_successfully.connect(self.load_entries)
        self.settings_window.autologout_activated.connect(self.start_autologout)
        self.settings_window.autologout_deactivated.connect(self.stop_autologout)
        self.settings_window.finished.connect(self.reset_settingswindow)
        self.settings_window.exec()

    def reset_settingswindow(self):
        self.settings_window = None

    def check_auto_backup(self):
        settings = load_settings()
        mode = settings.get("auto_backup", "none")
        last = settings.get("last_backup", None)
        now = datetime.now()
        
        if mode == "none":
            return
        
        if last is None:
            self.db.create_backup()
            settings["last_backup"] = now.isoformat()
            save_settings(settings)
            return
        
        last_dt = datetime.fromisoformat(last)
        do_backup = False
        if mode == "daily" and (now - last_dt).days >= 1:
            do_backup = True

        elif mode == "weekly" and (now - last_dt).days >= 7:
            do_backup = True

        elif mode == "monthly" and (
            now.year != last_dt.year or now.month != last_dt.month
        ):
            do_backup = True

        elif mode == "yearly" and now.year != last_dt.year:
            do_backup = True
        
        if do_backup:
            self.db.create_backup()
            settings["last_backup"] == now.isoformat()
            save_settings(settings)
            
    def filter_list(self, text: str):
        text = text.lower()
        self.ui.listWidget.clear()
        for entry in self.entry_cache:
            if (
                text in str(entry["id"]).lower() or
                text in entry["service"].lower() or
                text in entry["username"].lower() or
                text in entry["category"].lower()):
                widget = VaultListItemWidget(
                    entry["id"], entry["service"], entry["username"], entry["category"]
                )
                item = QListWidgetItem()
                item.setData(Qt.ItemDataRole.UserRole, entry["id"])
                item.setData(Qt.ItemDataRole.UserRole + 1, entry["service"])
                item.setData(Qt.ItemDataRole.UserRole + 2, entry["username"])
                item.setData(Qt.ItemDataRole.UserRole + 3, entry["category"])
                item.setSizeHint(widget.sizeHint())
                self.ui.listWidget.addItem(item)
                self.ui.listWidget.setItemWidget(item, widget)
    
    def hide_details_after_anim(self):
        self.ui.detailFrame.hide()
        self.ui.detailLabel.show()
        
    def toggle_details(self):
        frame = self.ui.detailFrame

        start = frame.width()
        end = self.details_max_width if not self.details_open else 0

        self.anim = QPropertyAnimation(frame, b"maximumWidth")
        self.anim.setDuration(350)
        self.anim.setStartValue(start)
        self.anim.setEndValue(end)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)  

        if self.details_open:
            self.anim.finished.connect(self.hide_details_after_anim)
        self.anim.start()
        self.details_open = not self.details_open