# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 572)
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.headerFrame = QFrame(MainWindow)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"border:0px;")
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.menuBtnFrame = QFrame(self.headerFrame)
        self.menuBtnFrame.setObjectName(u"menuBtnFrame")
        self.menuBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menuBtnFrame)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 0, 0, 0)
        self.btnSettings = QPushButton(self.menuBtnFrame)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(60, 15))
        font = QFont()
        font.setPointSize(9)
        self.btnSettings.setFont(font)

        self.horizontalLayout_4.addWidget(self.btnSettings)


        self.horizontalLayout.addWidget(self.menuBtnFrame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.titleFrame = QFrame(self.headerFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy)
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mainTitleIcon = QLabel(self.titleFrame)
        self.mainTitleIcon.setObjectName(u"mainTitleIcon")

        self.horizontalLayout_10.addWidget(self.mainTitleIcon)

        self.mainTitleLabel = QLabel(self.titleFrame)
        self.mainTitleLabel.setObjectName(u"mainTitleLabel")
        font1 = QFont()
        font1.setFamilies([u"Digital-7"])
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setItalic(False)
        self.mainTitleLabel.setFont(font1)
        self.mainTitleLabel.setStyleSheet(u"font: 26pt \"Digital-7\";")
        self.mainTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.mainTitleLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.btnLogout = QPushButton(self.titleFrame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(60, 15))

        self.horizontalLayout_10.addWidget(self.btnLogout)

        self.horizontalLayout_10.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.titleFrame)


        self.verticalLayout_2.addWidget(self.headerFrame)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(4)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(4, 4, 4, 4)
        self.sortFrame = QFrame(MainWindow)
        self.sortFrame.setObjectName(u"sortFrame")
        self.sortFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sortFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.sortFrame)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 2, 6, 2)
        self.sortByLabel = QLabel(self.sortFrame)
        self.sortByLabel.setObjectName(u"sortByLabel")

        self.horizontalLayout_8.addWidget(self.sortByLabel)

        self.sortBox = QComboBox(self.sortFrame)
        self.sortBox.setObjectName(u"sortBox")
        self.sortBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.sortBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.searchFrame = QFrame(self.sortFrame)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.searchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.searchLineEdit = QLineEdit(self.searchFrame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.searchLineEdit)


        self.horizontalLayout_8.addWidget(self.searchFrame)


        self.leftLayout.addWidget(self.sortFrame)

        self.listWidget = QListWidget(MainWindow)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMouseTracking(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSpacing(2)

        self.leftLayout.addWidget(self.listWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(6)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(4, -1, 4, -1)
        self.btnClearEntries = QPushButton(MainWindow)
        self.btnClearEntries.setObjectName(u"btnClearEntries")

        self.buttonLayout.addWidget(self.btnClearEntries)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_2)

        self.btnAdd = QPushButton(MainWindow)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(80, 30))

        self.buttonLayout.addWidget(self.btnAdd)

        self.btnDelete = QPushButton(MainWindow)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(80, 30))
        self.btnDelete.setStyleSheet(u"QPushButton::icon{\n"
"color: #fff;\n"
"}")

        self.buttonLayout.addWidget(self.btnDelete)


        self.leftLayout.addLayout(self.buttonLayout)


        self.mainLayout.addLayout(self.leftLayout)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setSpacing(0)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 485))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.detailLabel = QLabel(self.scrollAreaWidgetContents)
        self.detailLabel.setObjectName(u"detailLabel")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.detailLabel.setFont(font2)
        self.detailLabel.setStyleSheet(u"	color:rgb(118, 0, 0);	\n"
"font: bold 12pt \"Segoe UI\";")
        self.detailLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.detailLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.detailFrame = QFrame(self.scrollAreaWidgetContents)
        self.detailFrame.setObjectName(u"detailFrame")
        self.detailFrame.setEnabled(True)
        self.detailFrame.setMinimumSize(QSize(363, 0))
        self.detailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.detailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.detailFrame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.detailFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.detailTitle = QLabel(self.detailFrame)
        self.detailTitle.setObjectName(u"detailTitle")
        self.detailTitle.setFont(font2)
        self.detailTitle.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.detailTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.detailTitle)

        self.serviceFrame = QFrame(self.detailFrame)
        self.serviceFrame.setObjectName(u"serviceFrame")
        self.serviceHBox = QHBoxLayout(self.serviceFrame)
        self.serviceHBox.setSpacing(6)
        self.serviceHBox.setContentsMargins(11, 11, 11, 11)
        self.serviceHBox.setObjectName(u"serviceHBox")
        self.serviceHBox.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.serviceFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.serviceHBox.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.serviceLabel = QLabel(self.serviceFrame)
        self.serviceLabel.setObjectName(u"serviceLabel")
        sizePolicy.setHeightForWidth(self.serviceLabel.sizePolicy().hasHeightForWidth())
        self.serviceLabel.setSizePolicy(sizePolicy)

        self.serviceHBox.addWidget(self.serviceLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btnEditService = QPushButton(self.serviceFrame)
        self.btnEditService.setObjectName(u"btnEditService")

        self.serviceHBox.addWidget(self.btnEditService)


        self.verticalLayout.addWidget(self.serviceFrame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.usernameFrame = QFrame(self.detailFrame)
        self.usernameFrame.setObjectName(u"usernameFrame")
        self.usernameEditLayout = QHBoxLayout(self.usernameFrame)
        self.usernameEditLayout.setSpacing(6)
        self.usernameEditLayout.setContentsMargins(11, 11, 11, 11)
        self.usernameEditLayout.setObjectName(u"usernameEditLayout")
        self.usernameEditLayout.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.usernameFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.usernameEditLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.usernameLabel = QLabel(self.usernameFrame)
        self.usernameLabel.setObjectName(u"usernameLabel")
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)

        self.usernameEditLayout.addWidget(self.usernameLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btnEditUsername = QPushButton(self.usernameFrame)
        self.btnEditUsername.setObjectName(u"btnEditUsername")

        self.usernameEditLayout.addWidget(self.btnEditUsername)


        self.verticalLayout.addWidget(self.usernameFrame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.passFrame = QFrame(self.detailFrame)
        self.passFrame.setObjectName(u"passFrame")
        self.passEditLayout = QHBoxLayout(self.passFrame)
        self.passEditLayout.setSpacing(6)
        self.passEditLayout.setContentsMargins(11, 11, 11, 11)
        self.passEditLayout.setObjectName(u"passEditLayout")
        self.passEditLayout.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.passFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.passEditLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignVCenter)

        self.passLabel = QLabel(self.passFrame)
        self.passLabel.setObjectName(u"passLabel")
        sizePolicy.setHeightForWidth(self.passLabel.sizePolicy().hasHeightForWidth())
        self.passLabel.setSizePolicy(sizePolicy)

        self.passEditLayout.addWidget(self.passLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btnEditPass = QPushButton(self.passFrame)
        self.btnEditPass.setObjectName(u"btnEditPass")

        self.passEditLayout.addWidget(self.btnEditPass)


        self.verticalLayout.addWidget(self.passFrame, 0, Qt.AlignmentFlag.AlignVCenter)

        self.passSecurityFrame = QFrame(self.detailFrame)
        self.passSecurityFrame.setObjectName(u"passSecurityFrame")
        self.passEditLayout_2 = QHBoxLayout(self.passSecurityFrame)
        self.passEditLayout_2.setSpacing(6)
        self.passEditLayout_2.setContentsMargins(11, 11, 11, 11)
        self.passEditLayout_2.setObjectName(u"passEditLayout_2")
        self.passEditLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_9 = QLabel(self.passSecurityFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.passEditLayout_2.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignVCenter)

        self.indicatorHolder = QVBoxLayout()
        self.indicatorHolder.setSpacing(0)
        self.indicatorHolder.setObjectName(u"indicatorHolder")

        self.passEditLayout_2.addLayout(self.indicatorHolder)

        self.passEditLayout_2.setStretch(1, 2)

        self.verticalLayout.addWidget(self.passSecurityFrame)

        self.urlFrame = QFrame(self.detailFrame)
        self.urlFrame.setObjectName(u"urlFrame")
        self.urlFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.urlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.urlFrame)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.label_7 = QLabel(self.urlFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setSizeIncrement(QSize(0, 0))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignVCenter)

        self.urlLabel = QLabel(self.urlFrame)
        self.urlLabel.setObjectName(u"urlLabel")
        sizePolicy.setHeightForWidth(self.urlLabel.sizePolicy().hasHeightForWidth())
        self.urlLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.urlLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btnEditUrl = QPushButton(self.urlFrame)
        self.btnEditUrl.setObjectName(u"btnEditUrl")

        self.horizontalLayout_12.addWidget(self.btnEditUrl)


        self.verticalLayout.addWidget(self.urlFrame)

        self.categoryFrame = QFrame(self.detailFrame)
        self.categoryFrame.setObjectName(u"categoryFrame")
        self.categoryFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.categoryFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.categoryFrame)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.categoryFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.categoryLabel = QLabel(self.categoryFrame)
        self.categoryLabel.setObjectName(u"categoryLabel")
        sizePolicy.setHeightForWidth(self.categoryLabel.sizePolicy().hasHeightForWidth())
        self.categoryLabel.setSizePolicy(sizePolicy)
        self.categoryLabel.setMinimumSize(QSize(110, 0))
        self.categoryLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\"; border-radius: 5px; background: rgba(211, 211, 211, 140);")
        self.categoryLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.categoryLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.btnEditCategory = QPushButton(self.categoryFrame)
        self.btnEditCategory.setObjectName(u"btnEditCategory")

        self.horizontalLayout_7.addWidget(self.btnEditCategory)


        self.verticalLayout.addWidget(self.categoryFrame)

        self.createdFrame = QFrame(self.detailFrame)
        self.createdFrame.setObjectName(u"createdFrame")
        self.createdFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.createdFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.createdFrame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.createdFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.createdLabel = QLabel(self.createdFrame)
        self.createdLabel.setObjectName(u"createdLabel")
        sizePolicy.setHeightForWidth(self.createdLabel.sizePolicy().hasHeightForWidth())
        self.createdLabel.setSizePolicy(sizePolicy)
        self.createdLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.createdLabel)


        self.verticalLayout.addWidget(self.createdFrame)

        self.updatedFrame = QFrame(self.detailFrame)
        self.updatedFrame.setObjectName(u"updatedFrame")
        self.updatedFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.updatedFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.updatedFrame)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_6 = QLabel(self.updatedFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.updatedLabel = QLabel(self.updatedFrame)
        self.updatedLabel.setObjectName(u"updatedLabel")
        sizePolicy.setHeightForWidth(self.updatedLabel.sizePolicy().hasHeightForWidth())
        self.updatedLabel.setSizePolicy(sizePolicy)
        self.updatedLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.updatedLabel)


        self.verticalLayout.addWidget(self.updatedFrame)

        self.noteFrame = QFrame(self.detailFrame)
        self.noteFrame.setObjectName(u"noteFrame")
        self.noteFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.noteFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.noteFrame)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_8 = QLabel(self.noteFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	color:rgb(118, 0, 0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.noteLabel = QTextEdit(self.noteFrame)
        self.noteLabel.setObjectName(u"noteLabel")
        self.noteLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.noteLabel.sizePolicy().hasHeightForWidth())
        self.noteLabel.setSizePolicy(sizePolicy)
        self.noteLabel.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid rgb(60, 60, 60);      /* Subtle border */\n"
"    border-radius: 6px;\n"
"    selection-background-color: rgb(38, 79, 120);  /* VSCode-like selection */\n"
"    selection-color: #ffffff;\n"
"	font: 9pt \"Segoe UI\";\n"
"    padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid rgb(0, 222, 222);      /* Blue accent on focus */\n"
"}\n"
"")
        self.noteLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.noteLabel.setFrameShadow(QFrame.Shadow.Sunken)
        self.noteLabel.setReadOnly(True)
        self.noteLabel.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.noteLabel)

        self.btnEditNote = QPushButton(self.noteFrame)
        self.btnEditNote.setObjectName(u"btnEditNote")

        self.horizontalLayout_13.addWidget(self.btnEditNote, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.noteFrame)

        self.detailBtnFrame = QFrame(self.detailFrame)
        self.detailBtnFrame.setObjectName(u"detailBtnFrame")
        self.detailBtnFrame.setStyleSheet(u"border:0px;")
        self.detailBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.detailBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.detailBtnFrame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.staatusFrame = QFrame(self.detailBtnFrame)
        self.staatusFrame.setObjectName(u"staatusFrame")
        self.staatusFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.staatusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.staatusFrame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.detailStatus = QLabel(self.staatusFrame)
        self.detailStatus.setObjectName(u"detailStatus")

        self.verticalLayout_4.addWidget(self.detailStatus)


        self.verticalLayout_5.addWidget(self.staatusFrame)

        self.btnFrame = QFrame(self.detailBtnFrame)
        self.btnFrame.setObjectName(u"btnFrame")
        self.btnFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.btnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.btnFrame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.btnFrame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.btnShowPass = QPushButton(self.btnFrame)
        self.btnShowPass.setObjectName(u"btnShowPass")

        self.horizontalLayout_3.addWidget(self.btnShowPass)

        self.btnCopyPass = QPushButton(self.btnFrame)
        self.btnCopyPass.setObjectName(u"btnCopyPass")

        self.horizontalLayout_3.addWidget(self.btnCopyPass)

        self.btnCloseDetails = QPushButton(self.btnFrame)
        self.btnCloseDetails.setObjectName(u"btnCloseDetails")

        self.horizontalLayout_3.addWidget(self.btnCloseDetails)


        self.verticalLayout_5.addWidget(self.btnFrame, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.detailBtnFrame)


        self.verticalLayout_3.addWidget(self.detailFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.rightLayout.addWidget(self.scrollArea)


        self.mainLayout.addLayout(self.rightLayout)

        self.mainLayout.setStretch(0, 4)
        self.mainLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.mainLayout)

        self.footerFrame = QFrame(MainWindow)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setStyleSheet(u"border:0px;")
        self.footerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 2, 9, 2)
        self.footerLabel = QLabel(self.footerFrame)
        self.footerLabel.setObjectName(u"footerLabel")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        self.footerLabel.setFont(font4)
        self.footerLabel.setStyleSheet(u"QLabel {\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(125, 125, 125);\n"
"}")
        self.footerLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.footerLabel)


        self.verticalLayout_2.addWidget(self.footerFrame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PassTreasure - Vault", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.mainTitleIcon.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.mainTitleLabel.setText(QCoreApplication.translate("MainWindow", u"PassTreasure", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.sortByLabel.setText(QCoreApplication.translate("MainWindow", u"Sorted By:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.btnClearEntries.setText(QCoreApplication.translate("MainWindow", u"Clear Entries", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add New Entry", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.detailLabel.setText(QCoreApplication.translate("MainWindow", u"Select an entry to see details", None))
        self.detailTitle.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Service:", None))
        self.serviceLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditService.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditUsername.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditPass.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Security:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Url:", None))
        self.urlLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditUrl.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditCategory.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Created At", None))
        self.createdLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Updated At:", None))
        self.updatedLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Note:", None))
        self.noteLabel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No notice set...", None))
        self.btnEditNote.setText("")
        self.detailStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnShowPass.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.btnCopyPass.setText(QCoreApplication.translate("MainWindow", u"Copy Password", None))
        self.btnCloseDetails.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

