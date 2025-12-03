import os
import json
import sys
from pathlib import Path
from datetime import datetime

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
VAULT_PATH = resource_path('data/vault.db')
DATA_PATH = resource_path("data")

SETTINGS_PATH = resource_path("data/user_settings.json")
DEFAULT_SETTINGS = {
    "auto_backup": "daily",
    "last_backup": None
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
ENTRY_CATEGORYS = ["General", "Arbeit", "Privat", "Finanzen", "Sonstiges"]
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



class Styles:
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
        padding: 6px;
        border-radius: 6px;
    }

    QLineEdit:focus {
        border: 1px solid #007acc;
    }

    QPushButton {
        background-color: #2d2d30;
        border: 1px solid #3a3a3a;
        padding: 6px;
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
