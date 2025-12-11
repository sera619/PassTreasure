from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QFont
from src.category_popup_ui import Ui_CategoryPopup
from config import load_settings, save_settings
import resources_rc
import config
import utils

class CategoryPopup(QDialog):
    def __init__(self, service_name: str, parent=None, categories=None, current_category=None):
        super().__init__(parent)  # <-- Parent korrekt setzen
        self.ui = Ui_CategoryPopup()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.ui.label.setText(f"Wähle eine Kategorie für den Service:\n{service_name}")
        if categories is None:
            categories = ["General", "Arbeit", "Privat", "Finanzen", "Sonstiges"]

        self.ui.comboBoxCategory.addItems(categories)

        if current_category in categories:
            self.ui.comboBoxCategory.setCurrentText(current_category)

        self.ui.btnOK.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        self.ui.btnOK.setStyleSheet(config.Styles.green_button_outlined)
        self.ui.btnCancel.setStyleSheet(config.Styles.red_button_outlined)
        utils.colorize_icon(self.ui.btnCancel, "close", "red")
        utils.colorize_icon(self.ui.btnOK, "check", "green")      
        


    @property
    def selected_category(self):
        return self.ui.comboBoxCategory.currentText()
