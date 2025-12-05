import os
import json
import sys
from pathlib import Path
from datetime import datetime

IS_DEBUGGING = False

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

BASE_DIR = resource_path(".")
DATA_PATH = resource_path("data")
VAULT_PATH = resource_path('data/vault.db')
SETTINGS_PATH = resource_path("data/user_settings.json")
DEFAULT_SETTINGS = {
    "auto_backup": "daily",
    "last_backup": None,
    "auto_logout": True,
    "auto_logouttime": 180000, # 3 min
    "entry_categories": ["General", "Arbeit", "Privat", "Finanzen", "Sonstiges", "Social Media"],
    "category_colors": {
        "General": "rgba(211, 211, 211, 140)",    # LightGray
        "Arbeit": "rgba(70, 130, 180, 140)",      # SteelBlue
        "Privat": "rgba(144, 238, 144, 140)",     # LightGreen
        "Finanzen": "rgba(255, 215, 0, 140)",     # Gold
        "Sonstiges": "rgba(255, 165, 0, 140)",    # Orange
        "Social Media": "rgba(30, 195, 198, 180)" # Cyan  
    }
}

VERSION_NUM = "1.2.4"
TEST_ENTRIES = [
    {"service": "Gmail", "username": "nick.dev", "password": "Qm9!t5C8yN"},
    {"service": "Github", "username": "nick-codes", "password": "Wk3$az92Lp"},
    {"service": "StackOverflow", "username": "nick_hh", "password": "aP4!Rn63De"},
    {"service": "Discord", "username": "nick#1337", "password": "Jt7@Xh82Vu"},
    {"service": "Steam", "username": "nickgaming", "password": "Tg9!yU24Qk"},
    {"service": "EpicGames", "username": "nick_dev", "password": "Lp2#qF89Wv"},
    {"service": "Battle.net", "username": "nick-wow", "password": "Rm8&Ks72Hd"},
    {"service": "Netflix", "username": "nickflix", "password": "Qp1)Gr55Xv"},
    {"service": "Amazon", "username": "nickshop", "password": "Fh4*Le11Pq"},
    {"service": "PlayStation", "username": "nickpsn", "password": "Mj3/Sw84Dt"},
    {"service": "Xbox", "username": "nickxbox", "password": "Nc6!Pe19Ww"},
    {"service": "Spotify", "username": "nickmusic", "password": "Bz8?Er90Ht"},
    {"service": "Gitlab", "username": "nicklab", "password": "Vs5=Tg42Fy"},
    {"service": "DigitalOcean", "username": "nickcloud", "password": "Kd1@Vx67Bn"},
    {"service": "Hetzner", "username": "nick-vps", "password": "Pq3!Nz58Hr"},
    {"service": "Twitter", "username": "nickbird", "password": "Gs9%Kb44De"},
    {"service": "Reddit", "username": "nickreddit", "password": "Rj4!Ax73Ws"},
    {"service": "Facebook", "username": "nick.fb", "password": "Fm6)Qz88Hv"},
    {"service": "Instagram", "username": "nick_insta", "password": "Ht2?Sk51Lm"},
    {"service": "LinkedIn", "username": "nick-work", "password": "Zn7!Pt33Dq"},
    {"service": "ProtonMail", "username": "nickpm", "password": "Cv9*Hf72Ua"},
    {"service": "Outlook", "username": "nick-out", "password": "Wx6)Dr40Kv"},
    {"service": "Unity", "username": "nickunity", "password": "Bt4=Vy61Np"},
    {"service": "UnrealEngine", "username": "nickue", "password": "Jc8@Qr54Fw"},
    {"service": "Twitch", "username": "nicktv", "password": "Hf7&Zu88Qe"},
    {"service": "YouTube", "username": "nickyt", "password": "Kc3+Dp72Aa"},
    {"service": "Paypal", "username": "nickpay", "password": "Tm5?Yl91Wx"},
    {"service": "Banking", "username": "nick-bank", "password": "Ra8!Cq64Nz"},
    {"service": "Telegram", "username": "nicktg", "password": "Lp1!Op73Qs"},
    {"service": "Signal", "username": "nicksignal", "password": "Gx9#Dr26Pw"},
    {"service": "Ebay", "username": "nickbay", "password": "Nd5&Xw34Jv"},
    {"service": "Pinterest", "username": "nickpins", "password": "Qm7)Fa88Ls"},
    {"service": "Adobe", "username": "nickdesign", "password": "Rf2%Gt62Qq"},
    {"service": "Microsoft", "username": "nick-ms", "password": "Zw6?Rb45Yt"},
    {"service": "AWS", "username": "nickaws", "password": "Hp9*Xe31Nv"},
    {"service": "OpenAI", "username": "nickai", "password": "Jv3!Lm56Qw"},
    {"service": "Bitwarden", "username": "nick-test", "password": "Ct4)Yp82Hr"},
    {"service": "DockerHub", "username": "nickdocker", "password": "Pn8!Mv20Je"},
    {"service": "VMware", "username": "nickvm", "password": "Fr5=Qk67Sw"},
    {"service": "Mega", "username": "nickmega", "password": "Xy1*Hp93Td"}
]
ABOUT_TEXT = (
    "PassTreasure ist ein lokaler Passwort-Manager, der deine Daten sicher in einer "
    "verschlüsselten SQLite-Datenbank speichert. Keine Cloud, keine Telemetrie – alle "
    "Passwörter bleiben komplett offline.\n"
    "\n"
    "Features:\n"
    "• AES-256-GCM Verschlüsselung\n"
    "• Master-Passwort mit sicherer Key-Derivation\n"
    "• Passwörter hinzufügen, bearbeiten und löschen\n"
    "• Passwort-Visibility Toggle\n"
    "• Moderne PySide6-Oberfläche\n"
    "• Komplett offline, kein Tracking\n"
    "\n"
    "Sicherheit:\n"
    "• Passwort-Hashing über Argon2 / PBKDF2\n"
    "• Einzigartige Salt- und Nonce-Werte pro Eintrag\n"
    "• AES-GCM als authentifizierte Verschlüsselung\n"
    "• Der Master-Key verlässt nie das Gerät\n"
    "\n"
    "Über dieses Projekt:\n"
    "PassTreasure entstand als Lernprojekt im Bereich IT-Security, Python und "
    "GUI-Programmierung. Es wird aktiv weiterentwickelt und ausgebaut.\n"
    "\n"
    "Author:\n"
    "• S3R43o3\n"
    "\n"
    "Lizenz:\n"
    "Dieses Projekt steht unter der MIT License.\n"
    "Copyright (c) 2025 S3R43o3\n"
    "\n"
    f"Version: v{VERSION_NUM}\n"
    "Letztes Update: 02.12.2025\n"
)

def load_settings():
    if not SETTINGS_PATH.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS
    try:
        return json.loads(SETTINGS_PATH.read_text())
    except:
        return DEFAULT_SETTINGS
    
def save_settings(data):
    SETTINGS_PATH.write_text(json.dumps(data, indent=4))

def format_last_backup(iso_str: str) -> str:
    if not iso_str:
        return "Nie"

    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%d.%m.%Y %H:%M:%S")
    except Exception:
        return "Ungültig"

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


class TextStorage:
    PW_INDICATOR_STRENGTH_TEXTS = [
        "Danger Zone!",
        "Needs Work",
        "Not Bad",
        "Solid",
        "Fortress"
    ]

class Styles:
    green_button = """
        QPushButton {
            background-color: #1b5e20;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #2e7d32;
        }
        QPushButton:hover {
            background-color: #2e7d32;
        }
        QPushButton:pressed {
            background-color: #1b5e20;
        }"""

    red_button = """
        QPushButton {
            background-color: #8b1a1a;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #b71c1c;
        }
        QPushButton:hover {
            background-color: #b71c1c;
        }
        QPushButton:pressed {
            background-color: #7f0000;
        }"""

    blue_button = """
        QPushButton {
            background-color: #0d47a1;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #0d47a1;
        }
        QPushButton:hover {
           	background-color: #1565c0;
        }
        QPushButton:pressed {
            background-color: #0d47a1;
        }"""

    yellow_button = """
        QPushButton {
            background-color: #b8860b;
            color: #333;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #f9a825;
        }
        QPushButton:hover {
            background-color: #f9a825;
        }
        QPushButton:pressed {
            background-color: #f57f17;
        }"""

    yellow_button_low = """
        QPushButton {
            background-color: #b8860b;
            color: #333;
            padding: 2px 4px;
            border-radius: 4px;
            border: 1px solid #f9a825;
        }
        QPushButton:hover {
            background-color: #f9a825;
        }
        QPushButton:pressed {
            background-color: #f57f17;
        }"""

    dark_button = """
        QPushButton {
            background-color: #2c2c2c;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #1f1f1f;
        }
        QPushButton:hover {
            background-color: #3a3a3a;
        }
        QPushButton:pressed {
            background-color: #1a1a1a;
        }"""

    # ---------------------------------------------------------
    # 🔥 NEW OUTLINED BUTTONS
    # ---------------------------------------------------------

    green_button_outlined = """
        QPushButton {
            background: transparent;
            color: #1b5e20;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #2e7d32;
        }
        QPushButton:hover {
            background-color: rgba(46, 125, 50, 30);
        }
        QPushButton:pressed {
            background-color: rgba(27, 94, 32, 60);
        }"""

    red_button_outlined = """
        QPushButton {
            background: transparent;
            color: #8b1a1a;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #b71c1c;
        }
        QPushButton:hover {
            background-color: rgba(183, 28, 28, 30);
        }
        QPushButton:pressed {
            background-color: rgba(127, 0, 0, 60);
        }"""

    blue_button_outlined = """
        QPushButton {
            background: transparent;
            color: #0d47a1;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #1565c0;
        }
        QPushButton:hover {
            background-color: rgba(21, 101, 192, 30);
        }
        QPushButton:pressed {
            background-color: rgba(13, 71, 161, 60);
        }"""

    yellow_button_outlined = """
        QPushButton {
            background: transparent;
            color: #b8860b;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #f9a825;
        }
        QPushButton:hover {
            background-color: rgba(249, 168, 37, 30);
        }
        QPushButton:pressed {
            background-color: rgba(245, 127, 23, 60);
        }"""
    yellow_button_outlined_low = """
        QPushButton {
            background: transparent;
            color: #b8860b;
            padding: 2px 10px;
            border-radius: 6px;
            border: 1px solid #f9a825;
        }
        QPushButton:hover {
            background-color: rgba(249, 168, 37, 30);
        }
        QPushButton:pressed {
            background-color: rgba(245, 127, 23, 60);
        }"""
    dark_button_outlined = """
        QPushButton {
            background: transparent;
            color: #dcdcdc;
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid #3a3a3a;
        }
        QPushButton:hover {
            background-color: rgba(255, 255, 255, 20);
        }
        QPushButton:pressed {
            background-color: rgba(255, 255, 255, 40);
        }"""

    list_widget_style = """
        QListWidget::item:hover {
                background-color: rgba(255, 255, 255, 20);
                border-radius: 4px;
            }

            QListWidget::item:selected {
                background-color: rgba(255, 255, 255, 40);
                border-radius: 4px;
            }

        """
    
    dark_style = """
        QWidget {
            background-color: #1e1e1e;
            color: #dcdcdc;
            font-family: Segoe UI;
            font-size: 14px;
        }

        QLineEdit {
            background-color: #2b2b2b;
            border: 1px solid #3a3a3a;
            padding: 4px;
            border-radius: 6px;
        }

        QLineEdit:focus {
            border: 1px solid #007acc;
        }

        QPushButton {
            background-color: #2d2d30;
            border: 1px solid #3a3a3a;
            padding: 4px;
            border-radius: 6px;
        }

        QPushButton:hover {
            background-color: #3a3a3a;
        }

        QPushButton:pressed {
            background-color: #007acc;
            color: white;
        }

        QMessageBox {
            background-color: #1e1e1e;
            color: #dcdcdc;
        }
        """
