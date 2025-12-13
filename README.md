<center>


![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![PySide6](https://img.shields.io/badge/GUI-PySide6-6f42c1)
![Encryption](https://img.shields.io/badge/Encryption-AES--256--GCM-red)
![KDF](https://img.shields.io/badge/KDF-Argon2id%20%7C%20PBKDF2-yellow)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![Platform](https://img.shields.io/badge/Platform-Local%20Only-orange)
![Database](https://img.shields.io/badge/Database-Encrypted%20SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)


</center>

# PassTreasure

PassTreasure is a fully local password manager that stores all data securely in an encrypted SQLite database.  
No cloud. No telemetry. No tracking. Everything stays on your device — and belongs only to you.

---

## 🔽 Download (Releases)

You can now download standalone ZIP or Windows Installer builds directly from the GitHub Releases page.
Perfect if you just want to run the app without installing anything.

👉 Check it out here: [Releases](https://github.com/sera619/PassTreasure/releases) → Download the latest ZIP or Installer

---

## 🚀 Features

### 🔐 Security & Encryption
- AES-256-GCM encryption  
- Strong key derivation: **Argon2id** or **PBKDF2-HMAC-SHA256**  
- Unique salt & nonce values for every entry  
- Master key never leaves the device  
- 100% offline — zero network communication  
- Encrypted SQLite vault with automatic integrity checks

### 🖥️ Interface & User Experience
- Modern and clean **PySide6** UI  
- Auto-logout with adjustable timer  
- Create & modify categories for password organization  
- Fast search and filtering
- Custom notice for each password
- Time-based Secure Clipboard
- Automatic check for Update
- Smooth animations (expanding detail views, fade transitions, etc.)
- Detail panel with password notes, meta info and timestamps
  
### 🔧 Additional Tools
- Password generator with real-time strength analysis  
- Manual and automatic vault backups  
- Import passwords from Firefox and Chrome  
- Robust error handling and logging  
- Export passwords as .json or .csv

## 🛠️ Under the Hood
- Packaging via PyInstaller & cx_Freeze
- Cross-platform compatibility (Windows / Linux, macOS coming later)

---

## 📦 Installation

```bash
git clone https://github.com/sera619/PassTreasure.git
cd PassTreasure
pip install -r requirements.txt
python main.py
```


