from PySide6.QtWidgets import (
    QApplication,QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget,
    QPushButton, QLineEdit, QInputDialog, QMessageBox, QTextEdit,QListWidgetItem, QToolTip
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer, Signal
from src.mainwindow_ui import Ui_MainWindow
from gui.change_password_popup import ChangePasswordPopup
from gui.settings_window import SettingsWindow
from gui.category_popup import CategoryPopup
from gui.vault_listiem import VaultListItemWidget
from backend.database import PasswordDatabase
from config import VERSION_NUM, load_settings, save_settings, Styles
from datetime import datetime

class MainWindow(QWidget):
    logout_success = Signal()
    def __init__(self, db: PasswordDatabase):
        super().__init__()
        self.db = db  # unlocked PasswordDatabase instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_cache = []
        self.setWindowTitle("PassTreasure - Vault")
        self.apply_dark_theme()
        self.build_ui()  
        self.apply_styles()
        loaded_entries = self.db.get_all_entries()
        # if len(loaded_entries) == 0:
        #     self.db.add_test_entries()
        self._block_click = False
        self.load_entries()
        self.check_auto_backup()
        QTimer.singleShot(0, self.clear_initial_selection)
            
    # Dark Theme
    def apply_dark_theme(self):
        self.setStyleSheet(Styles.dark_style)

    def apply_styles(self):
        self.ui.btnSettings.setStyleSheet(Styles.blue_button_outlined)
        self.ui.btnLogout.setStyleSheet(Styles.red_button_outlined)
        self.ui.btnAdd.setStyleSheet(Styles.green_button_outlined)
        self.ui.btnDelete.setStyleSheet(Styles.red_button_outlined)

        self.ui.btnEditCategory.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditPass.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditService.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditUsername.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnEditUrl.setStyleSheet(Styles.yellow_button_outlined_low)
        self.ui.btnClearEntries.setStyleSheet(Styles.red_button)
        self.ui.btnCopyPass.setStyleSheet(Styles.dark_button)
        self.ui.btnShowPass.setStyleSheet(Styles.dark_button)
        self.ui.listWidget.setStyleSheet(Styles.list_widget_style)
        self.ui.btnCloseDetails.setStyleSheet(Styles.red_button_outlined)
    
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
            "Kategorie"
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
        
    def hide_details(self):
        self.ui.detailFrame.hide()
        self.ui.btnDelete.hide()

    def sort_list(self, role_key):
        self.entry_cache.sort(key= lambda e: e[role_key])
        self.render_list()
        
    def sort_by_selection(self):
        text = self.ui.sortBox.currentText()
        if text == "Kategorie":
            self.sort_list("category")
        elif text == "Service":
            self.sort_list("service")
        elif text == "Username":
            self.sort_list("username")
        elif text == "ID":
            self.sort_list("id")          
     
    def logout(self):
        self.logout_success.emit()
        self.close()     
        
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
            QMessageBox.critical(self, "Error", f"Failed to load entries:\n{e}")

    # -------------------------
    # Update detail view
    # -------------------------
    def close_details(self):
        self.ui.listWidget.setCurrentItem(None)
        self.hide_details()
      
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
            
            self.ui.serviceLabel.setText(service)
            self.ui.usernameLabel.setText(username)
            self.ui.passLabel.setText("•" * len(pw))
            self.ui.categoryLabel.setText(category)
            self.ui.urlLabel.setText(details.get("url"))
            
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
        service, ok1 = QInputDialog.getText(self, "Service", "Enter service name:")
        if not ok1 or not service.strip():
            return
        username, ok2 = QInputDialog.getText(self, "Username", "Enter username:")
        if not ok2 or not username.strip():
            return
        pass_dialog = ChangePasswordPopup(parent=self)
        if pass_dialog.exec():
            password = pass_dialog.get_password()
        
        settings = load_settings()
        entry_categories = settings.get("entry_categories")
        category_dialog = CategoryPopup(service_name=service.strip(), categories=entry_categories, parent=self)
        if category_dialog.exec():
            category = category_dialog.selected_category
        
        if not password:
            import secrets, string
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(chars) for _ in range(16))

        try:
            self.db.add_entry(service.strip(), username.strip(), password, category)
            self.load_entries()
            QMessageBox.information(self, "Success", f"Entry added!\nService: {service.strip()}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add entry:\n{e}")

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
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete entry:\n{e}")
         
    def clear_all_entries(self):
        confirm = QMessageBox.question(self, "Confirm Clear", "Are you sure you want delete ALL entries?")
        if confirm != QMessageBox.StandardButton.Yes:
            return
        try:
            self.db.clear_entries()
            self.load_entries()
            self.hide_details()
            QMessageBox.information(self, "Clear Successfully", "Entries successfully cleared!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to clear entries:\n{e}")
    
    def edit_entry_username(self):
        selected =  self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()
        if not selected:
            return
        
        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        current_username = self.ui.usernameLabel.text()
        new_username, ok = QInputDialog.getText(
            self,
            "Edit Username",
            f"Enter new username:\n(current: {current_username})",
            text=current_username
        )
        
        if not ok or not new_username.strip():
            return
        
        try:
            self.db.edit_username(entry_id, new_username.strip())
            self.load_entries()
            # self.ui.listWidget.setCurrentRow(self.ui.listWidget.count() - 1)
            self.update_details(selected)
            self.ui.listWidget.setCurrentIndex(index)
        except Exception as e:
            QMessageBox.critical(self, "ERROR", f"Failed to update username:\n{e}")
    
    def edit_entry_password(self):
        selected = self.ui.listWidget.currentItem()
        index = self.ui.listWidget.currentIndex()

        if not selected:
            return
        service_name = self.ui.serviceLabel.text()
        entry_id = selected.data(Qt.ItemDataRole.UserRole)
        current_password = self.db.get_password(entry_id)

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
                QMessageBox.information(self, "Success", f"Password updated for:\n{service_name}")

            except Exception as e:
                QMessageBox.critical(self, "ERROR", f"Failed to update password:\n{e}")
    
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
                QMessageBox.information(self, "Success", f"Category updated for:\n{service_name}")

            except Exception as e:
                QMessageBox.critical(self, "ERROR", f"Failed to update category:\n{e}")            
    
    def edit_entry_service(self):
        selected = self.ui.listWidget.currentItem()
        if not selected:
            return

        entry_id = selected.data(Qt.ItemDataRole.UserRole)

        current_service = self.ui.serviceLabel.text()
        new_service, ok = QInputDialog.getText(
            self,
            "Edit Service",
            "Enter new service name:",
            text=current_service
        )

        if not ok or not new_service.strip():
            return

        try:
            self.db.edit_service(entry_id, new_service.strip())
            self.load_entries()
            self.update_details(self.ui.listWidget.currentItem())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update service:\n{e}")
            
    def edit_entry_url(self):        
        selected = self.ui.listWidget.currentItem()
        if not selected:
            return

        entry_id = selected.data(Qt.ItemDataRole.UserRole)

        current_service = self.ui.serviceLabel.text()
        current_url = self.ui.urlLabel.text()
        new_url, ok = QInputDialog.getText(
            self,
            "Edit Url",
            f"Enter new url for service:\n\n'{current_service}'",
            text=current_url,
        )

        if not ok or not new_url.strip():
            return

        try:
            self.db.edit_url(entry_id, new_url.strip())
            self.load_entries()
            self.update_details(self.ui.listWidget.currentItem())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update url:\n{e}")
            
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
        dig = SettingsWindow(self.db)
        dig.category_deleted.connect(self.load_entries)
        dig.backup_restored.connect(self.load_entries)
        dig.category_updated.connect(self.load_entries)
        dig.import_successfully.connect(self.load_entries)
        dig.exec()

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