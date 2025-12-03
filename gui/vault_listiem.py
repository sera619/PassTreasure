from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from src.vaultlistitemwidget_ui import Ui_VaultListItemWidget  # Pfad zu deiner generierten UI

class VaultListItemWidget(QWidget):
    category_colors = {
        "General": "rgba(211, 211, 211, 140)",    # LightGray
        "Arbeit": "rgba(70, 130, 180, 140)",      # SteelBlue
        "Privat": "rgba(144, 238, 144, 140)",     # LightGreen
        "Finanzen": "rgba(255, 215, 0, 140)",     # Gold
        "Sonstiges": "rgba(255, 165, 0, 140)"     # Orange
    }

    def __init__(self, entry_id: int, service: str, username: str, category: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_VaultListItemWidget()
        self.ui.setupUi(self)

        self.ui.labelText.setText(f"{entry_id}: {service} ({username})")

        self.ui.badgeLabel.setText(category)
        color = self.category_colors.get(category, "rgba(211, 211, 211, 140)")
        self.ui.badgeLabel.setStyleSheet(
            f'font: 700 8pt "Segoe UI"; border-radius: 5px; background: {color};'
        )
        self.ui.badgeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
