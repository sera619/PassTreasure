from PySide6.QtWidgets import QApplication
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

def open_main(db_instance):
    global main_window
    main_window = None
    main_window = MainWindow(db_instance)
    main_window.setWindowIcon(QIcon(":/assets/icon.png"))
    main_window.logout_success.connect(restart_login)
    main_window.show()
    
def restart_login():
    global login
    login = None
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
    