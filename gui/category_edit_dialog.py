from PySide6.QtWidgets import QDialog, QColorDialog
from PySide6.QtGui import QColor, QIcon
from src.category_edit_dialog_ui import Ui_CategoryEditDialog
import resources_rc
import config
import utils

class CategoryEditDialog(QDialog):
    def __init__(self, current_name: str, current_color: str, parent = None):
        super().__init__(parent)
        self.ui = Ui_CategoryEditDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.setWindowTitle("Edit Category")
        self._apply_style()
        # Init UI values
        self.ui.lineEdit_name.setText(current_name)
        self.color = QColor(current_color)
        self.ui.button_colorPreview.setStyleSheet(
            "QPushButton:disabled{"
            f"background-color: {current_color}; border-radius: 4px;"
            "}"
        )

        # Signals
        self.ui.button_pickColor.clicked.connect(self.pick_color)
        self.ui.button_save.clicked.connect(self.accept)
        self.ui.button_cancel.clicked.connect(self.reject)

    def _apply_style(self):
        self.ui.button_pickColor.setStyleSheet(config.Styles.yellow_button_outlined)
        self.ui.button_cancel.setStyleSheet(config.Styles.red_button_outlined)
        self.ui.button_save.setStyleSheet(config.Styles.green_button_outlined)
        
        utils.colorize_icon(self.ui.button_cancel, "close", "red")
        utils.colorize_icon(self.ui.button_pickColor, "eyedropper", "yellow")
        utils.colorize_icon(self.ui.button_save, "check", "green")        
        
    def pick_color(self):
        dialog = QColorDialog(self.color)
        dialog.setOptions( QColorDialog.ColorDialogOption.ShowAlphaChannel | 
                          QColorDialog.ColorDialogOption.DontUseNativeDialog)
        dialog.setCurrentColor(self.color)
        if dialog.exec() == QColorDialog.DialogCode.Accepted:
            picked_color = dialog.selectedColor()
            self.color = picked_color
            self.ui.button_colorPreview.setStyleSheet(
                "QPushButton:disabled{"
                f"background-color: {self.color.name()}; border-radius: 4px;"
                "}"
            )

    def get_results(self):
        return (
            self.ui.lineEdit_name.text().strip(),
            self.color.name()
        )