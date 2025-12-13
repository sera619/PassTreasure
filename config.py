from utils import get_base_dir
from enum import Enum
import os

IS_DEBUGGING = False
VERSION_NUM = "2.2.5"
GITHUB_API = "https://api.github.com/repos/sera619/PassTreasure/releases/latest"
    
BASE_DIR = get_base_dir()
DATA_PATH = os.path.join(BASE_DIR, "data")
BACKUP_PATH = os.path.join(BASE_DIR, "backup")
SETTINGS_PATH = os.path.join(DATA_PATH, "settings.json")
VAULT_PATH = os.path.join(DATA_PATH, "vault.db")

EXPORT_TYPES = [
    ".json",
    ".csv"
]

DEFAULT_SETTINGS: dict = {
    "auto_backup": "daily",
    "last_backup": None,
    "backup_path": f"{BACKUP_PATH}",
    "check_update": False,
    "auto_logout": True,
    "auto_logouttime": 180000, # 3 min
    "auto_hide_details": False,
    "auto_hide_details_time": 60000, # 60 sec
    "entry_categories": ["General", "Work", "Private", "Finance", "Others", "Social Media"],
    "category_colors": {
        "General": "rgba(211, 211, 211, 180)",    # LightGray
        "Work": "rgba(70, 130, 180, 180)",      # SteelBlue
        "Private": "rgba(144, 238, 144, 180)",     # LightGreen
        "Finance": "rgba(255, 215, 0, 180)",     # Gold
        "Others": "rgba(255, 165, 0, 180)",    # Orange
        "Social Media": "rgba(30, 195, 198, 180)" # Cyan  
    }
}

class PopupType(Enum):
    SUCCESS = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    QUESTION = 5

class TextStorage:
    PW_INDICATOR_STRENGTH_TEXTS = [
        "Danger Zone!",
        "Needs Work",
        "Not Bad",
        "Solid",
        "Fortress"
    ]
    ABOUT_TEXT = f"""
        <h3 style="color:#ff4444; margin:0; padding:0;">PassTreasure</h3>
        <p style="margin-top:6px;">
            PassTreasure is a fully local password manager that securely stores your data in an
            encrypted SQLite database. No cloud, no telemetry, no tracking — everything stays offline.
        </p>

        <h4 style="color:#66b3ff; margin-bottom:4px; margin-top:14px;">Features</h4>
        <ul style="margin-top:0;">
            <li>AES-256-GCM encryption</li>
            <li>Strong key derivation (Argon2id / PBKDF2-HMAC-SHA256)</li>
            <li>Add, edit and delete password entries</li>
            <li>Modern PySide6 interface</li>
            <li>Auto-logout with configurable timer</li>
            <li>Customizable password generator</li>
            <li>Custom categories for entries</li>
            <li>Vault backup (manual & automatic)</li>
            <li>Import from Firefox/Chrome</li>
            <li>Search and filtering</li>
        </ul>

        <h4 style="color:#8cff66; margin-bottom:4px; margin-top:14px;">Security</h4>
        <ul style="margin-top:0;">
            <li>Argon2id / PBKDF2 key derivation</li>
            <li>Unique salt & nonce per entry</li>
            <li>Authenticated AES-GCM encryption</li>
            <li>Master key never leaves the device</li>
            <li>No cloud services involved</li>
        </ul>

        <h4 style="color:#ffaa44; margin-bottom:4px; margin-top:14px;">About</h4>
        <p style="margin-top:0;">
            PassTreasure started as a learning project focused on Python, cryptography and GUI
            programming. It is actively maintained and expanded.
        </p>

        <p style="margin-top:20px; font-size:11px; color:#888;">
            <b>Author:</b> S3R43o3<br>
            <b>License:</b> MIT License<br>
            <b>Version:</b> v{VERSION_NUM}
        </p>"""

class Styles:
    COLORS = {
        "green": "#1b5e20",
        "yellow": "#b8860b",
        "blue": "#0d47a1",
        "red": "#8b1a1a",
        "dark": "#ffffff"        
    }
    
    h_line = """  
       background-color: rgb(97, 97, 97);
    """
    green_button = """
        QPushButton {
            background-color: #1b5e20;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
            border: 0.5px solid #2e7d32;
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
            border: 0.5px solid #b71c1c;
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
            padding: 3px 6px;
            border-radius: 6px;
            border: 0.5px solid #0d47a1;
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
            border: 0.5px solid #f9a825;
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
            border: 0.5px solid #f9a825;
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
            border: 0.5px solid #1f1f1f;
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
            border: 0.5px solid #2e7d32;
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
            border: 0.5px solid #b71c1c;
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
            padding: 3px 6px;
            border-radius: 6px;
            border: 0.5px solid #1565c0;
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
            border: 0.5px solid #f9a825;
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
            padding: 2px 6px;
            border-radius: 6px;
            border: 0.5px solid #f9a825;
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
            border: 0.5px solid #3a3a3a;
        }
        QPushButton:hover {
            background-color: rgba(0, 255, 255, 20);
        }
        QPushButton:pressed {
            background-color: rgba(0, 255, 255, 40);
        }"""


    dark_style = """

        QWidget {
            background-color: #1e1e1e;
            color: #dcdcdc;
            font-family: Segoe UI;
            font-size: 12px;
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
            padding: 3px 6px;
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
        

TEST_ENTRIES: list = [
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