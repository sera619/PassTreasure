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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 535)
        self.verticalLayout_2 = QVBoxLayout(MainWindow)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
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
        self.btnSettings.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnSettings)

        self.btnLogout = QPushButton(self.menuBtnFrame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(60, 15))

        self.horizontalLayout_4.addWidget(self.btnLogout)


        self.horizontalLayout.addWidget(self.menuBtnFrame, 0, Qt.AlignmentFlag.AlignLeft)

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

        self.horizontalLayout_10.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.titleFrame)


        self.verticalLayout_2.addWidget(self.headerFrame)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(4)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(4)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(2, -1, 2, -1)
        self.frame_2 = QFrame(MainWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.detailLabel = QLabel(self.frame_2)
        self.detailLabel.setObjectName(u"detailLabel")
        self.detailLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.detailLabel)

        self.sortFrame = QFrame(self.frame_2)
        self.sortFrame.setObjectName(u"sortFrame")
        self.sortFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sortFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.sortFrame)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.sortByLabel = QLabel(self.sortFrame)
        self.sortByLabel.setObjectName(u"sortByLabel")

        self.horizontalLayout_8.addWidget(self.sortByLabel)

        self.sortBox = QComboBox(self.sortFrame)
        self.sortBox.setObjectName(u"sortBox")
        self.sortBox.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.sortBox)


        self.horizontalLayout_9.addWidget(self.sortFrame)


        self.leftLayout.addWidget(self.frame_2)

        self.searchFrame = QFrame(MainWindow)
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


        self.leftLayout.addWidget(self.searchFrame)

        self.listWidget = QListWidget(MainWindow)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMouseTracking(True)
        self.listWidget.setAlternatingRowColors(True)

        self.leftLayout.addWidget(self.listWidget)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(6)
        self.buttonLayout.setObjectName(u"buttonLayout")
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

        self.buttonLayout.addWidget(self.btnDelete)


        self.leftLayout.addLayout(self.buttonLayout)


        self.mainLayout.addLayout(self.leftLayout)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setSpacing(4)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(4, 4, 4, 4)
        self.detailFrame = QFrame(MainWindow)
        self.detailFrame.setObjectName(u"detailFrame")
        self.detailFrame.setEnabled(True)
        self.detailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.detailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.detailFrame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.detailFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.detailTitle = QLabel(self.detailFrame)
        self.detailTitle.setObjectName(u"detailTitle")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.detailTitle.setFont(font2)
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

        self.horizontalLayout_7.addWidget(self.categoryLabel)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

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


        self.rightLayout.addWidget(self.detailFrame, 0, Qt.AlignmentFlag.AlignVCenter)


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
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.mainTitleIcon.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.mainTitleLabel.setText(QCoreApplication.translate("MainWindow", u"PassTreasure", None))
        self.detailLabel.setText(QCoreApplication.translate("MainWindow", u"Select an entry to see details", None))
        self.sortByLabel.setText(QCoreApplication.translate("MainWindow", u"Sorted By:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.btnClearEntries.setText(QCoreApplication.translate("MainWindow", u"Clear Entries", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add New Entry", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.detailTitle.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Service:", None))
        self.serviceLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditService.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditUsername.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditPass.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Url:", None))
        self.urlLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditUrl.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnEditCategory.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Created At", None))
        self.createdLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Updated At:", None))
        self.updatedLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.detailStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnShowPass.setText(QCoreApplication.translate("MainWindow", u"Show Password", None))
        self.btnCopyPass.setText(QCoreApplication.translate("MainWindow", u"Copy Password", None))
        self.btnCloseDetails.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

