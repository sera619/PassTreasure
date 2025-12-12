from PySide6.QtGui import QPixmap, QPainter, QColor, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
import config 
import json
import resources_rc
import sys
import os
import requests
from pathlib import Path
from datetime import datetime


def has_internet(timeout: float = 2.0) -> bool:
    """check if system has active internet conntection"""
    try:
        requests.get("https://1.1.1.1", timeout=timeout)
        return True 
    except requests.RequestException:
        return False

def open_url(url: str):
    import webbrowser
    webbrowser.open(url)

def parse_version(version: str) -> tuple:
    """Convert version string like '2.2.7' to tuple (2, 2, 7)"""
    return tuple(map(int, version.split(".")))

def check_for_update():
    """Check GitHub for latest release and compare with local version"""
    if not has_internet():
        return
    try:
        response = requests.get(config.GITHUB_API, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        latest_version = data["tag_name"].lstrip("v")
        download_url = data["assets"][0]["browser_download_url"]
        
        
        local_v = parse_version(config.VERSION_NUM)
        remote_v = parse_version(latest_version)
        
        if remote_v > local_v:
            return {
                "update_available": True,
                "version": latest_version,
                "download_url": download_url,
                "changelog": data.get("body", "")
                }
        else:
            return {"update_available": False}
    except Exception as e:
        return {"error": str(e)}

def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)
    
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
    if not os.path.exists(config.SETTINGS_PATH):
        save_settings(config.DEFAULT_SETTINGS)
        return config.DEFAULT_SETTINGS
    try:
        with open(config.SETTINGS_PATH, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            return data
    except:
        return config.DEFAULT_SETTINGS
    
def save_settings(data):
    with open(config.SETTINGS_PATH, "w", encoding="utf-8") as f:
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