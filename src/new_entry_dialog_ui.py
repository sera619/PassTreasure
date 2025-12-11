# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_entry_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_NewEntryDialog(object):
    def setupUi(self, NewEntryDialog):
        if not NewEntryDialog.objectName():
            NewEntryDialog.setObjectName(u"NewEntryDialog")
        NewEntryDialog.resize(475, 775)
        self.verticalLayout_3 = QVBoxLayout(NewEntryDialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.scrollArea = QScrollArea(NewEntryDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 467, 767))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"Line {\n"
"background-color: rgb(97, 97, 97);\n"
"}")
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: bold 11pt \"Segoe UI\";")

        self.verticalLayout_9.addWidget(self.label)

        self.labelError = QLabel(self.frame)
        self.labelError.setObjectName(u"labelError")
        font1 = QFont()
        font1.setBold(True)
        self.labelError.setFont(font1)
        self.labelError.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.labelError.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.labelError)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.serviceLayout = QHBoxLayout()
        self.serviceLayout.setObjectName(u"serviceLayout")
        self.serviceLayout.setContentsMargins(-1, 4, -1, 4)
        self.newServiceInput = QLineEdit(self.frame)
        self.newServiceInput.setObjectName(u"newServiceInput")

        self.serviceLayout.addWidget(self.newServiceInput)

        self.btnClearService = QPushButton(self.frame)
        self.btnClearService.setObjectName(u"btnClearService")
        self.btnClearService.setAutoDefault(False)

        self.serviceLayout.addWidget(self.btnClearService)


        self.verticalLayout_2.addLayout(self.serviceLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_4)

        self.usernameLayout = QHBoxLayout()
        self.usernameLayout.setObjectName(u"usernameLayout")
        self.usernameLayout.setContentsMargins(-1, 4, -1, 4)
        self.newUsernameInput = QLineEdit(self.frame)
        self.newUsernameInput.setObjectName(u"newUsernameInput")

        self.usernameLayout.addWidget(self.newUsernameInput)

        self.btnClearUsername = QPushButton(self.frame)
        self.btnClearUsername.setObjectName(u"btnClearUsername")
        self.btnClearUsername.setAutoDefault(False)

        self.usernameLayout.addWidget(self.btnClearUsername)


        self.verticalLayout_4.addLayout(self.usernameLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, 4)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_5)

        self.pw1Layout = QHBoxLayout()
        self.pw1Layout.setObjectName(u"pw1Layout")
        self.pw1Input = QLineEdit(self.frame)
        self.pw1Input.setObjectName(u"pw1Input")

        self.pw1Layout.addWidget(self.pw1Input)

        self.btnClearPw1 = QPushButton(self.frame)
        self.btnClearPw1.setObjectName(u"btnClearPw1")
        self.btnClearPw1.setAutoDefault(False)

        self.pw1Layout.addWidget(self.btnClearPw1)


        self.verticalLayout.addLayout(self.pw1Layout)

        self.indicatorHolder = QVBoxLayout()
        self.indicatorHolder.setSpacing(0)
        self.indicatorHolder.setObjectName(u"indicatorHolder")
        self.indicatorHolder.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout.addLayout(self.indicatorHolder)

        self.pw2Layout = QHBoxLayout()
        self.pw2Layout.setObjectName(u"pw2Layout")
        self.pw2Input = QLineEdit(self.frame)
        self.pw2Input.setObjectName(u"pw2Input")

        self.pw2Layout.addWidget(self.pw2Input)

        self.btnClearPw2 = QPushButton(self.frame)
        self.btnClearPw2.setObjectName(u"btnClearPw2")
        self.btnClearPw2.setAutoDefault(False)

        self.pw2Layout.addWidget(self.btnClearPw2)


        self.verticalLayout.addLayout(self.pw2Layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnGeneratePw = QPushButton(self.frame)
        self.btnGeneratePw.setObjectName(u"btnGeneratePw")
        self.btnGeneratePw.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnGeneratePw)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pwVisibilityCheck = QCheckBox(self.frame)
        self.pwVisibilityCheck.setObjectName(u"pwVisibilityCheck")

        self.horizontalLayout.addWidget(self.pwVisibilityCheck)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.label_6)

        self.urlLayout = QHBoxLayout()
        self.urlLayout.setObjectName(u"urlLayout")
        self.urlLayout.setContentsMargins(-1, 4, -1, 4)
        self.urlInput = QLineEdit(self.frame)
        self.urlInput.setObjectName(u"urlInput")

        self.urlLayout.addWidget(self.urlInput)

        self.btnClearUrl = QPushButton(self.frame)
        self.btnClearUrl.setObjectName(u"btnClearUrl")
        self.btnClearUrl.setAutoDefault(False)

        self.urlLayout.addWidget(self.btnClearUrl)


        self.verticalLayout_5.addLayout(self.urlLayout)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.categoryComboBox = QComboBox(self.frame)
        self.categoryComboBox.setObjectName(u"categoryComboBox")
        self.categoryComboBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.categoryComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.noteTextEdit = QTextEdit(self.frame)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        self.noteTextEdit.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.noteTextEdit)

        self.btnClearNote = QPushButton(self.frame)
        self.btnClearNote.setObjectName(u"btnClearNote")
        self.btnClearNote.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.btnClearNote, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_9.addWidget(self.buttonBox)


        self.verticalLayout_8.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(NewEntryDialog)
        self.buttonBox.accepted.connect(NewEntryDialog.accept)
        self.buttonBox.rejected.connect(NewEntryDialog.reject)

        QMetaObject.connectSlotsByName(NewEntryDialog)
    # setupUi

    def retranslateUi(self, NewEntryDialog):
        NewEntryDialog.setWindowTitle(QCoreApplication.translate("NewEntryDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NewEntryDialog", u"Add a new Entry to your vault.", None))
        self.labelError.setText(QCoreApplication.translate("NewEntryDialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("NewEntryDialog", u"Service:", None))
        self.newServiceInput.setText("")
        self.newServiceInput.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Enter a service...", None))
        self.btnClearService.setText("")
        self.label_4.setText(QCoreApplication.translate("NewEntryDialog", u"Username:", None))
        self.newUsernameInput.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Enter a username...", None))
        self.btnClearUsername.setText("")
        self.label_5.setText(QCoreApplication.translate("NewEntryDialog", u"Password:", None))
        self.pw1Input.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Enter a password...", None))
        self.btnClearPw1.setText("")
        self.pw2Input.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Repeat your password...", None))
        self.btnClearPw2.setText("")
        self.btnGeneratePw.setText(QCoreApplication.translate("NewEntryDialog", u"Generate Password", None))
        self.pwVisibilityCheck.setText(QCoreApplication.translate("NewEntryDialog", u"Show Password", None))
        self.label_6.setText(QCoreApplication.translate("NewEntryDialog", u"Url:", None))
        self.urlInput.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Enter a url...", None))
        self.btnClearUrl.setText("")
        self.label_7.setText(QCoreApplication.translate("NewEntryDialog", u"Category:", None))
        self.label_2.setText(QCoreApplication.translate("NewEntryDialog", u"Select a category", None))
        self.categoryComboBox.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Select category...", None))
        self.label_8.setText(QCoreApplication.translate("NewEntryDialog", u"Note:", None))
        self.noteTextEdit.setPlaceholderText(QCoreApplication.translate("NewEntryDialog", u"Enter a note here...", None))
        self.btnClearNote.setText("")
    # retranslateUi

