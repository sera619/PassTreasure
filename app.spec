# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

app_name = "PassTreasure"

# --- CRYPTO hidden imports ---
hiddenimports = collect_submodules("cryptography")

# --- QT plugins (richtig!) ---
qt_plugins = ["platforms", "styles", "iconengines", "imageformats"]
qt_binaries = []

for plugin in qt_plugins:
    qt_binaries += collect_data_files(f"PySide6/Qt/plugins/{plugin}")

# --- Data files ---
datas = [
    ("assets", "assets"),
    ("backend", "backend"),
    ("gui", "gui"),
    ("src", "src"),
    ("utils.py", "."),
    ("config.py", "."),
    ("resources_rc.py", "."),
    ("app.ico", "."),
    ("LICENCE", "."),
    ("README.md", ".")
]

# --- ANALYSIS ---
a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=qt_binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    noarchive=False,
)

pyz = PYZ(a.pure)

# --- EXE (KORREKTE REIHENFOLGE!!!) ---
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=app_name,
    debug=False,
    strip=True,
    upx=True,
    console=False,
    icon="app.ico",
)

# --- COLLECT ---
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    a.zipfiles,
    name=app_name
)
