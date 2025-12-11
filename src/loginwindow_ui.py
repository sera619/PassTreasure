# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindowUI(object):
    def setupUi(self, LoginWindowUI):
        if not LoginWindowUI.objectName():
            LoginWindowUI.setObjectName(u"LoginWindowUI")
        LoginWindowUI.resize(400, 278)
        self.verticalLayout = QVBoxLayout(LoginWindowUI)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 4)
        self.headerFrame = QFrame(LoginWindowUI)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_icon = QLabel(self.headerFrame)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_icon)

        self.label_header = QLabel(self.headerFrame)
        self.label_header.setObjectName(u"label_header")
        self.label_header.setStyleSheet(u"font: 28pt \"Digital-7\";")
        self.label_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_header)


        self.verticalLayout.addWidget(self.headerFrame)

        self.label = QLabel(LoginWindowUI)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_title = QLabel(LoginWindowUI)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.frame = QFrame(LoginWindowUI)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.input_password = QLineEdit(self.frame)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.input_password)

        self.btn_toggle_pw = QPushButton(self.frame)
        self.btn_toggle_pw.setObjectName(u"btn_toggle_pw")
        font1 = QFont()
        font1.setPointSize(9)
        self.btn_toggle_pw.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_toggle_pw, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.indicatorHolder = QVBoxLayout()
        self.indicatorHolder.setSpacing(0)
        self.indicatorHolder.setObjectName(u"indicatorHolder")
        self.indicatorHolder.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout.addLayout(self.indicatorHolder)

        self.pw2Frame = QFrame(LoginWindowUI)
        self.pw2Frame.setObjectName(u"pw2Frame")
        self.pw2Frame.setFrameShape(QFrame.Shape.NoFrame)
        self.pw2Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.pw2Frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.input_password2 = QLineEdit(self.pw2Frame)
        self.input_password2.setObjectName(u"input_password2")

        self.horizontalLayout_2.addWidget(self.input_password2)

        self.btn_toggle_pw2 = QPushButton(self.pw2Frame)
        self.btn_toggle_pw2.setObjectName(u"btn_toggle_pw2")

        self.horizontalLayout_2.addWidget(self.btn_toggle_pw2)


        self.verticalLayout.addWidget(self.pw2Frame)

        self.label_error = QLabel(LoginWindowUI)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"color: #ff4444;")
        self.label_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_error.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_error)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(9)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.btn_restore_backup = QPushButton(LoginWindowUI)
        self.btn_restore_backup.setObjectName(u"btn_restore_backup")

        self.buttonLayout.addWidget(self.btn_restore_backup)

        self.btn_delete_vault = QPushButton(LoginWindowUI)
        self.btn_delete_vault.setObjectName(u"btn_delete_vault")

        self.buttonLayout.addWidget(self.btn_delete_vault)

        self.btn_login = QPushButton(LoginWindowUI)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setVisible(True)

        self.buttonLayout.addWidget(self.btn_login)

        self.btn_create = QPushButton(LoginWindowUI)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setVisible(True)

        self.buttonLayout.addWidget(self.btn_create)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.footer_label = QLabel(LoginWindowUI)
        self.footer_label.setObjectName(u"footer_label")
        self.footer_label.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"color: rgb(75, 75, 75);")

        self.verticalLayout.addWidget(self.footer_label, 0, Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(LoginWindowUI)

        QMetaObject.connectSlotsByName(LoginWindowUI)
    # setupUi

    def retranslateUi(self, LoginWindowUI):
        LoginWindowUI.setWindowTitle(QCoreApplication.translate("LoginWindowUI", u"PassTreasure - Login", None))
        self.label_icon.setText(QCoreApplication.translate("LoginWindowUI", u"TextLabel", None))
        self.label_header.setText(QCoreApplication.translate("LoginWindowUI", u"PassTreasure", None))
        self.label.setText(QCoreApplication.translate("LoginWindowUI", u"Welcome!", None))
        self.label_title.setText(QCoreApplication.translate("LoginWindowUI", u"Enter Master Password:", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("LoginWindowUI", u"Enter master password...", None))
        self.btn_toggle_pw.setText(QCoreApplication.translate("LoginWindowUI", u"Show", None))
        self.input_password2.setPlaceholderText(QCoreApplication.translate("LoginWindowUI", u"Repeat master password...", None))
        self.btn_toggle_pw2.setText(QCoreApplication.translate("LoginWindowUI", u"Show", None))
        self.label_error.setText("")
        self.btn_restore_backup.setText(QCoreApplication.translate("LoginWindowUI", u"Restore Backup", None))
        self.btn_delete_vault.setText(QCoreApplication.translate("LoginWindowUI", u"Delete Vault", None))
        self.btn_login.setText(QCoreApplication.translate("LoginWindowUI", u"Login", None))
        self.btn_create.setText(QCoreApplication.translate("LoginWindowUI", u"Create Vault", None))
        self.footer_label.setText(QCoreApplication.translate("LoginWindowUI", u"TextLabel", None))
    # retranslateUi

