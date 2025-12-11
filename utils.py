from PySide6.QtGui import QPixmap, QPainter, QColor, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
import config
import resources_rc


def tint_pixmap(pix: QPixmap, color: QColor) -> QPixmap:
    """Recolors a pixmap fully with a given color."""
    tinted = QPixmap(pix.size())
    tinted.fill(Qt.GlobalColor.transparent)

    painter = QPainter(tinted)
    painter.drawPixmap(0, 0, pix)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(tinted.rect(), color)
    painter.end()
    return tinted

def colorize_icon(btn: QPushButton, icon: str, color: str) -> QPushButton:
    pixmap = QPixmap(f":/assets/{icon}.png")
    color = QColor(config.Styles.COLORS[color])
    colored = tint_pixmap(pixmap, color)
    icon = QIcon(colored)
    btn.setIcon(icon);
    return btn;