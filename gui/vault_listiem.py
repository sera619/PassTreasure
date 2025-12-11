from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from src.vaultlistitemwidget_ui import Ui_VaultListItemWidget  # Pfad zu deiner generierten UI
from utils import load_settings, limit_text

class VaultListItemWidget(QWidget):
    def __init__(self, entry_id: int, service: str, username: str, category: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_VaultListItemWidget()
        self.ui.setupUi(self)
        text = f"{entry_id}: {service} ({username})"
        self.ui.labelText.setText(limit_text(text, 52))

        self.ui.badgeLabel.setText(category)
        settings = load_settings()
        self.category_colors = settings.get("category_colors")
        
        color = self.category_colors.get(category, "rgba(211, 211, 211, 140)")
        self.ui.badgeLabel.setStyleSheet(
            f'font: 700 8pt "Segoe UI"; border-radius: 5px; background: {color};'
        )
        self.ui.badgeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
