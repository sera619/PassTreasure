# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingswindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(600, 400)
        SettingsWindow.setMinimumSize(QSize(600, 400))
        self.main_layout = QHBoxLayout(SettingsWindow)
        self.main_layout.setObjectName(u"main_layout")
        self.sidebar = QFrame(SettingsWindow)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.vboxLayout = QVBoxLayout(self.sidebar)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.btn_general = QPushButton(self.sidebar)
        self.btn_general.setObjectName(u"btn_general")

        self.vboxLayout.addWidget(self.btn_general)

        self.btn_security = QPushButton(self.sidebar)
        self.btn_security.setObjectName(u"btn_security")

        self.vboxLayout.addWidget(self.btn_security)

        self.btn_about = QPushButton(self.sidebar)
        self.btn_about.setObjectName(u"btn_about")

        self.vboxLayout.addWidget(self.btn_about)

        self.sidebar_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.sidebar_spacer)


        self.main_layout.addWidget(self.sidebar)

        self.stack = QStackedWidget(SettingsWindow)
        self.stack.setObjectName(u"stack")
        self.page_general = QWidget()
        self.page_general.setObjectName(u"page_general")
        self.vboxLayout1 = QVBoxLayout(self.page_general)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.label_2 = QLabel(self.page_general)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignTop)

        self.backupFrame = QFrame(self.page_general)
        self.backupFrame.setObjectName(u"backupFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backupFrame.sizePolicy().hasHeightForWidth())
        self.backupFrame.setSizePolicy(sizePolicy)
        self.backupFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.backupFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backupFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.backupTitleLabel = QLabel(self.backupFrame)
        self.backupTitleLabel.setObjectName(u"backupTitleLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.backupTitleLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.backupTitleLabel)

        self.autoBackupFrame = QFrame(self.backupFrame)
        self.autoBackupFrame.setObjectName(u"autoBackupFrame")
        self.autoBackupFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.autoBackupFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.autoBackupFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_4 = QLabel(self.autoBackupFrame)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.backupModeBox = QComboBox(self.autoBackupFrame)
        self.backupModeBox.setObjectName(u"backupModeBox")
        self.backupModeBox.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.backupModeBox)


        self.verticalLayout_2.addWidget(self.autoBackupFrame)

        self.lastBackupFrame = QFrame(self.backupFrame)
        self.lastBackupFrame.setObjectName(u"lastBackupFrame")
        self.lastBackupFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.lastBackupFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.lastBackupFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_3 = QLabel(self.lastBackupFrame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.backUpPathLabel = QLabel(self.lastBackupFrame)
        self.backUpPathLabel.setObjectName(u"backUpPathLabel")

        self.horizontalLayout_3.addWidget(self.backUpPathLabel)


        self.verticalLayout_2.addWidget(self.lastBackupFrame)

        self.backupBtnFrame = QFrame(self.backupFrame)
        self.backupBtnFrame.setObjectName(u"backupBtnFrame")
        self.horizontalLayout = QHBoxLayout(self.backupBtnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCreateBackup = QPushButton(self.backupBtnFrame)
        self.btnCreateBackup.setObjectName(u"btnCreateBackup")

        self.horizontalLayout.addWidget(self.btnCreateBackup)

        self.btnRestoreBackup = QPushButton(self.backupBtnFrame)
        self.btnRestoreBackup.setObjectName(u"btnRestoreBackup")

        self.horizontalLayout.addWidget(self.btnRestoreBackup)

        self.btnDeleteBackup = QPushButton(self.backupBtnFrame)
        self.btnDeleteBackup.setObjectName(u"btnDeleteBackup")

        self.horizontalLayout.addWidget(self.btnDeleteBackup)

        self.btnClearBackup = QPushButton(self.backupBtnFrame)
        self.btnClearBackup.setObjectName(u"btnClearBackup")
        self.btnClearBackup.setStyleSheet(u"background: rgb(170, 0, 0);")

        self.horizontalLayout.addWidget(self.btnClearBackup)


        self.verticalLayout_2.addWidget(self.backupBtnFrame)


        self.vboxLayout1.addWidget(self.backupFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout1.addItem(self.verticalSpacer)

        self.stack.addWidget(self.page_general)
        self.page_security = QWidget()
        self.page_security.setObjectName(u"page_security")
        self.vboxLayout2 = QVBoxLayout(self.page_security)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.securityTitle = QLabel(self.page_security)
        self.securityTitle.setObjectName(u"securityTitle")
        self.securityTitle.setFont(font)
        self.securityTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.securityTitle)

        self.label = QLabel(self.page_security)
        self.label.setObjectName(u"label")

        self.vboxLayout2.addWidget(self.label)

        self.pw_frame = QFrame(self.page_security)
        self.pw_frame.setObjectName(u"pw_frame")
        self.pw_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.vboxLayout3 = QVBoxLayout(self.pw_frame)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.oldPwLabel = QLabel(self.pw_frame)
        self.oldPwLabel.setObjectName(u"oldPwLabel")

        self.vboxLayout3.addWidget(self.oldPwLabel)

        self.old_pw = QLineEdit(self.pw_frame)
        self.old_pw.setObjectName(u"old_pw")
        self.old_pw.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout3.addWidget(self.old_pw)

        self.newPwLabel = QLabel(self.pw_frame)
        self.newPwLabel.setObjectName(u"newPwLabel")

        self.vboxLayout3.addWidget(self.newPwLabel)

        self.new_pw1 = QLineEdit(self.pw_frame)
        self.new_pw1.setObjectName(u"new_pw1")
        self.new_pw1.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout3.addWidget(self.new_pw1)

        self.repeatPwLabel = QLabel(self.pw_frame)
        self.repeatPwLabel.setObjectName(u"repeatPwLabel")

        self.vboxLayout3.addWidget(self.repeatPwLabel)

        self.new_pw2 = QLineEdit(self.pw_frame)
        self.new_pw2.setObjectName(u"new_pw2")
        self.new_pw2.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout3.addWidget(self.new_pw2)

        self.btn_apply_pw = QPushButton(self.pw_frame)
        self.btn_apply_pw.setObjectName(u"btn_apply_pw")

        self.vboxLayout3.addWidget(self.btn_apply_pw)


        self.vboxLayout2.addWidget(self.pw_frame)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.spacerItem)

        self.stack.addWidget(self.page_security)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.vboxLayout4 = QVBoxLayout(self.page_about)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.aboutTitle = QLabel(self.page_about)
        self.aboutTitle.setObjectName(u"aboutTitle")
        self.aboutTitle.setFont(font)
        self.aboutTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout4.addWidget(self.aboutTitle, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.page_about)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 67, 32))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutLabel = QLabel(self.scrollAreaWidgetContents)
        self.aboutLabel.setObjectName(u"aboutLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aboutLabel.sizePolicy().hasHeightForWidth())
        self.aboutLabel.setSizePolicy(sizePolicy1)
        self.aboutLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.aboutLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.aboutLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.vboxLayout4.addWidget(self.scrollArea)

        self.stack.addWidget(self.page_about)

        self.main_layout.addWidget(self.stack)


        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.btn_general.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.btn_security.setText(QCoreApplication.translate("SettingsWindow", u"Security", None))
        self.btn_about.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.backupTitleLabel.setText(QCoreApplication.translate("SettingsWindow", u"Backups", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Auto. Updaes:", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Last Backup:", None))
        self.backUpPathLabel.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.btnCreateBackup.setText(QCoreApplication.translate("SettingsWindow", u"Create Backup", None))
        self.btnRestoreBackup.setText(QCoreApplication.translate("SettingsWindow", u"Restore Backup", None))
        self.btnDeleteBackup.setText(QCoreApplication.translate("SettingsWindow", u"Delete Backup", None))
        self.btnClearBackup.setText(QCoreApplication.translate("SettingsWindow", u"Clear Backups", None))
        self.securityTitle.setText(QCoreApplication.translate("SettingsWindow", u"Security", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Change Master Password", None))
        self.oldPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Old Password:", None))
        self.newPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"New Password:", None))
        self.repeatPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Repeat Password:", None))
        self.btn_apply_pw.setText(QCoreApplication.translate("SettingsWindow", u"Apply", None))
        self.aboutTitle.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.aboutLabel.setText(QCoreApplication.translate("SettingsWindow", u"PassTreasure v1.0", None))
    # retranslateUi

