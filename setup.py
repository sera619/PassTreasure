from cx_Freeze import Executable, setup
from config import VERSION_NUM
import sys
import os

include_files =[
    ("assets", "assets"),
    ("backend", "backend"),
    ("src", "src"),
    ("gui", "gui"),
    "resources_rc.py",
    "config.py"
]

build_exe_options = {
    "packages": [
        "PySide6",
        "cryptography",
        "backend",
        "gui",
        "src"
    ],
    "excludes": [
        "tkinter",
        "disnake",
        "aiohttp",
    ],
    "includes": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtSql",      # Nicht notwendig, aber schadet nicht
        "cryptography.hazmat.primitives.ciphers.aead"
    ],
    "include_files": include_files,
    "include_msvcr": True
}
    
target = Executable(
    script="main.py",
    base="Win32GUI",
    target_name="PassTreasure",
    copyright='Copyright (c) 2025, S3R43o3',
    shortcut_name='PassTreasure'
)


setup(
    name = "PassTreasure",
    version = f"{VERSION_NUM}",
    author="S3R43o3",
    description = "Passwordmanager for Windows.",
    options = {"build_exe": build_exe_options},
    executables = [target]
)