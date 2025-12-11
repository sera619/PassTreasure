from cx_Freeze import Executable, setup
from config import VERSION_NUM
import sys
import os
    
include_files = [
    ("assets", "assets"),
    # ("backend", "backend"),
    # ("src", "src"),
    # ("gui", "gui"),
    "resources_rc.py"
]

# Minimal benötigte Qt DLLs
bin_includes = [
    "Qt6Core.dll",
    "Qt6Gui.dll",
    "Qt6Widgets.dll",
    "Qt6Svg.dll",
    "Qt6SvgWidgets.dll",
]

build_exe_options = {
    "packages": [
        "PySide6",
        "cryptography",
        "backend",
        "gui",
        "src"
    ],
       # Alles raus, was nur aufbläht
    "excludes": [
        "tkinter",
        "disnake",
        "aiohttp",
        "unittest",
        "email",
        "http",
        "xmlrpc",
        "pydoc",
        "lib2to3",
        "distutils",
        # "asyncio",   # wenn du's nicht nutzt
        # "logging",   # falls du kein Logging benutzt
        # PySide6-Großmüll 
        "PySide6.Qt3DCore",
        "PySide6.Qt3D", 
        "PySide6.Qt3DRender", 
        "PySide6.Qt3DExtras", 
        "PySide6.QtCharts", 
        "PySide6.QtQuick", 
        "PySide6.QtQuickWidgets", 
        "PySide6.QtQuick3D", 
        "PySide6.QtTextToSpeech", 
        "PySide6.QtSensors", 
        "PySide6.QtQml", 
        "PySide6.Qt3DAnimation",
        "PySide6.Qt3DInput",
        "PySide6.Qt3DLogic", 
        "PySide6.QtGraphs", 
        "PySide6.QtHttpServer", 
        "PySide6.QtNetworkAuth", 
        "PySide6.QtRemoteObjects", 
        "PySide6.QtMultimediaWidgets",
        "PySide6.QtLocation", 
        "PySide6.QtSerialBus",
        "PySide6.QtGraphsWidgets", 
        "PySide6.QtDataVisualization", 
        "PySide6.QtMultimedia", 
        "PySide6.QtWebEngineWidgets", 
        "PySide6.QtWebEngineCore",
        "PySide6.QtWebEngineQuick",
        "PySide6.QtNetwork", # brauchst du NICHT für Standard-Widgets 
        "PySide6.QtWebSockets", 
        "PySide6.QtOpenGL", 
        "PySide6.QtOpenGLWidgets", 
        "PySide6.QtBluetooth", 
        "PySide6.QtNfc", 
        "PySide6.QtHelp", 
        "PySide6.QtPdf", 
        "PySide6.QtPdfWidgets", 
        "PySide6.QtPositioning", 
        "PySide6.QtSensors", 
        "PySide6.QtSerialPort", 
        "PySide6.QtStateMachine", 
        "PySide6.QtTest", 
        "PySide6.QtPrintSupport", # nur drin lassen, wenn du Printdialoge nutzt
    ],

    # Nur die Core-Qt-Module rein
    "includes": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "cryptography.hazmat.primitives.ciphers.aead"
    ],
    
    "bin_includes": bin_includes,    
    
    "bin_excludes": [
        "Qt6OpenGL.dll",
        "Qt6OpenGLWidgets.dll",
        "Qt6Network.dll",
        "Qt6Pdf.dll",
        "Qt6PdfWidgets.dll",
        "Qt6Qml.dll",
        "Qt6Quick.dll",
        "Qt6Quick3D.dll",
        "Qt6Multimedia.dll",
        "Qt6Charts.dll",
        "Qt6ChartsQml.dll",
        "Qt6Sensors.dll",
        "d3dcompiler_47.dll",
        "opengl32sw.dll",
        "libEGL.dll",
        "libGLESv2.dll",
    ],
    
    "include_files": include_files,
    "include_msvcr": False,
    "silent_level": 1,
    "optimize": 2,
    "zip_exclude_packages": ["PySide6"],
    "zip_include_packages": ["*"],
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