

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![PySide6](https://img.shields.io/badge/GUI-PySide6-6f42c1)
![Encryption](https://img.shields.io/badge/Encryption-AES--256--GCM-red)
![KDF](https://img.shields.io/badge/KDF-Argon2id%20%7C%20PBKDF2-yellow)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![Platform](https://img.shields.io/badge/Platform-Local%20Only-orange)
![Database](https://img.shields.io/badge/Database-Encrypted%20SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)


# PassTreasure

PassTreasure is a fully local password manager that stores all data securely in an encrypted SQLite database.  
No cloud. No telemetry. No tracking. Everything stays on your device — and belongs only to you.

---

## 🚀 Features

### 🔐 Security & Encryption
- AES-256-GCM encryption  
- Strong key derivation: **Argon2id** or **PBKDF2-HMAC-SHA256**  
- Unique salt & nonce values for every entry  
- Master key never leaves the device  
- 100% offline — zero network communication  

### 🖥️ Interface & User Experience
- Modern and clean **PySide6** UI  
- Auto-logout with adjustable timer  
- Custom categories for password organization  
- Fast search and filtering  

### 🔧 Additional Tools
- Password generator with real-time strength analysis  
- Manual and automatic vault backups  
- Import passwords from Firefox and Chrome  
- Robust error handling and logging  

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/PassTreasure.git
cd PassTreasure
pip install -r requirements.txt
python main.py

