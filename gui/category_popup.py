from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QFont
from src.category_popup_ui import Ui_CategoryPopup
import resources_rc

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

    @property
    def selected_category(self):
        return self.ui.comboBoxCategory.currentText()
