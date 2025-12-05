from PySide6.QtWidgets import QDialog, QColorDialog
from PySide6.QtGui import QColor, QIcon
from src.category_edit_dialog_ui import Ui_CategoryEditDialog
import resources_rc

class CategoryEditDialog(QDialog):
    def __init__(self, current_name: str, current_color: str, parent = None):
        super().__init__(parent)
        self.ui = Ui_CategoryEditDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.setWindowTitle("Edit Category")
        
        # Init UI values
        self.ui.lineEdit_name.setText(current_name)
        self.color = QColor(current_color)
        self.ui.button_colorPreview.setStyleSheet(
            f"background-color: {current_color}; border-radius: 4px;"
        )

        # Signals
        self.ui.button_pickColor.clicked.connect(self.pick_color)
        self.ui.button_save.clicked.connect(self.accept)
        self.ui.button_cancel.clicked.connect(self.reject)
        
    def pick_color(self):
        new_c = QColorDialog.getColor(self.color, self)
        if new_c.isValid():
            self.color = new_c
            self.ui.button_colorPreview.setStyleSheet(
                f"background-color: {new_c.name()}; border-radius: 4px;"
            )

    def get_results(self):
        return (
            self.ui.lineEdit_name.text().strip(),
            self.color.name()
        )