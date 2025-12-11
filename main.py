from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from gui.login_window import LoginWindow
from gui.main_window import MainWindow
from gui.intro_splash import IntroSplash

import config
from config import Styles
import sys
import resources_rc

app = QApplication([])
main_window = None
splash = None
login = None

def autologout_restart():
    global login
    login.show()
    login.close()
    login = None
    login = LoginWindow()
    login.setWindowIcon(QIcon(":/assets/icon.png"))
    login.login_success.connect(open_main)
    login.show()
    QMessageBox.information(login, "PassTreasure - Autologout", "You was a long time inactive.\nFor security reasons, you got logged out!\nBye!")
    
def open_main(db_instance):
    global main_window
    global login
    main_window = MainWindow(db_instance)
    main_window.setWindowIcon(QIcon(":/assets/icon.png"))
    main_window.logout_success.connect(restart_login)
    main_window.auto_logout_success.connect(autologout_restart)
    main_window.show()
    
def restart_login():
    global login
    global main_window
    login = None
    main_window = None
    login = LoginWindow()
    login.setWindowIcon(QIcon(":/assets/icon.png"))
    login.login_success.connect(open_main)
    login.show()

def start_login(splash):
    splash.close()
    global login
    login = LoginWindow()
    login.setWindowIcon(QIcon(":/assets/icon.png"))
    login.login_success.connect(open_main)
    login.show()

def main():
    app.setStyleSheet(Styles.dark_style)
    app.setApplicationVersion(f"v{config.VERSION_NUM}")
    global splash
    splash = IntroSplash()
    speed_up = config.IS_DEBUGGING
    if speed_up:
        splash = IntroSplash(200, 100)
    splash.setWindowIcon(QIcon(":/assets/icon.png"))
    splash.show()
    splash.start()
    splash.intro_finished.connect(lambda: start_login(splash))

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    