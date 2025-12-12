from PySide6.QtGui import QPixmap, QPainter, QColor, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
import config
import json
import resources_rc
import sys
import os
from pathlib import Path
from datetime import datetime

def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)
    
BASE_DIR = get_base_dir()
DATA_PATH = os.path.join(BASE_DIR, "data")
BACKUP_PATH = os.path.join(BASE_DIR, "backup")
SETTINGS_PATH = os.path.join(DATA_PATH, "settings.json")
VAULT_PATH = os.path.join(DATA_PATH, "vault.db")

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

def resource_path(relative: str) -> Path:
    """
    Get absolute path to resource, works in dev and PyInstaller exe.
    """
    try:
        # PyInstaller temp folder
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        # normal script
        if getattr(sys, 'frozen', False):
            base_path = Path(sys.executable).parent  # exe mode
        else:
            base_path = Path(__file__).parent       # dev mode
    return base_path / relative

def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        save_settings(config.DEFAULT_SETTINGS)
        return config.DEFAULT_SETTINGS
    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            return data
    except:
        return config.DEFAULT_SETTINGS
    
def save_settings(data):
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4))

def format_last_backup(iso_str: str) -> str:
    if not iso_str:
        return "Never"
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%d.%m.%Y %H:%M:%S")
    except Exception:
        return "Invalid"

def clean_url(url: str) -> str:
    if not url:
        return url

    url = url.strip()

    for prefix in ("https://", "http://", "www."):
        if url.startswith(prefix):
            url = url[len(prefix):]

    return url

def limit_text(text: str, max_len: int = 20) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."