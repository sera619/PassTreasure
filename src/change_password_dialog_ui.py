# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        if not ChangePasswordDialog.objectName():
            ChangePasswordDialog.setObjectName(u"ChangePasswordDialog")
        ChangePasswordDialog.resize(243, 230)
        self.vboxLayout = QVBoxLayout(ChangePasswordDialog)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.labelInfo = QLabel(ChangePasswordDialog)
        self.labelInfo.setObjectName(u"labelInfo")

        self.vboxLayout.addWidget(self.labelInfo)

        self.lineEditPassword1 = QLineEdit(ChangePasswordDialog)
        self.lineEditPassword1.setObjectName(u"lineEditPassword1")
        self.lineEditPassword1.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout.addWidget(self.lineEditPassword1)

        self.lineEditPassword2 = QLineEdit(ChangePasswordDialog)
        self.lineEditPassword2.setObjectName(u"lineEditPassword2")
        self.lineEditPassword2.setEchoMode(QLineEdit.EchoMode.Password)

        self.vboxLayout.addWidget(self.lineEditPassword2)

        self.check_show_pass = QCheckBox(ChangePasswordDialog)
        self.check_show_pass.setObjectName(u"check_show_pass")

        self.vboxLayout.addWidget(self.check_show_pass, 0, Qt.AlignmentFlag.AlignRight)

        self.btnGeneratePw = QPushButton(ChangePasswordDialog)
        self.btnGeneratePw.setObjectName(u"btnGeneratePw")

        self.vboxLayout.addWidget(self.btnGeneratePw, 0, Qt.AlignmentFlag.AlignRight)

        self.labelError = QLabel(ChangePasswordDialog)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelError.setWordWrap(True)

        self.vboxLayout.addWidget(self.labelError)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(ChangePasswordDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.vboxLayout.addWidget(self.buttonBox)


        self.retranslateUi(ChangePasswordDialog)

        QMetaObject.connectSlotsByName(ChangePasswordDialog)
    # setupUi

    def retranslateUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setWindowTitle(QCoreApplication.translate("ChangePasswordDialog", u"Change Password", None))
        self.labelInfo.setText(QCoreApplication.translate("ChangePasswordDialog", u"Please enter your new password twice:", None))
        self.lineEditPassword1.setPlaceholderText(QCoreApplication.translate("ChangePasswordDialog", u"Enter new  password...", None))
        self.lineEditPassword2.setPlaceholderText(QCoreApplication.translate("ChangePasswordDialog", u"Repeat new password...", None))
        self.check_show_pass.setText(QCoreApplication.translate("ChangePasswordDialog", u"Show Password", None))
        self.btnGeneratePw.setText(QCoreApplication.translate("ChangePasswordDialog", u"Generate Password", None))
        self.labelError.setStyleSheet(QCoreApplication.translate("ChangePasswordDialog", u"#labelError { color: red; }", None))
        self.labelError.setText("")
    # retranslateUi

