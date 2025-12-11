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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(630, 410)
        SettingsWindow.setMinimumSize(QSize(600, 400))
        self.main_layout = QHBoxLayout(SettingsWindow)
        self.main_layout.setObjectName(u"main_layout")
        self.sidebar = QFrame(SettingsWindow)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.vboxLayout = QVBoxLayout(self.sidebar)
        self.vboxLayout.setSpacing(4)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(6, 6, 6, 6)
        self.btn_general = QPushButton(self.sidebar)
        self.btn_general.setObjectName(u"btn_general")

        self.vboxLayout.addWidget(self.btn_general)

        self.btn_security = QPushButton(self.sidebar)
        self.btn_security.setObjectName(u"btn_security")

        self.vboxLayout.addWidget(self.btn_security)

        self.btn_import = QPushButton(self.sidebar)
        self.btn_import.setObjectName(u"btn_import")

        self.vboxLayout.addWidget(self.btn_import)

        self.btn_export = QPushButton(self.sidebar)
        self.btn_export.setObjectName(u"btn_export")

        self.vboxLayout.addWidget(self.btn_export)

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
        self.vboxLayout1.setContentsMargins(4, 4, 4, 4)
        self.label_2 = QLabel(self.page_general)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: bold 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollAreaGeneral = QScrollArea(self.page_general)
        self.scrollAreaGeneral.setObjectName(u"scrollAreaGeneral")
        self.scrollAreaGeneral.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGeneral.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -208, 489, 830))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.autoLogoutFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.autoLogoutFrame.setObjectName(u"autoLogoutFrame")
        self.autoLogoutFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.autoLogoutFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.autoLogoutFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.autoLogoutFrame)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_15.addWidget(self.label_10)

        self.frame_8 = QFrame(self.autoLogoutFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 5, 0, 5)
        self.line_6 = QFrame(self.frame_8)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.autoLogoutFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(130, 0))
        font2 = QFont()
        font2.setBold(True)
        self.label_11.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.autoLogoutTimeEdit = QTimeEdit(self.frame_9)
        self.autoLogoutTimeEdit.setObjectName(u"autoLogoutTimeEdit")
        self.autoLogoutTimeEdit.setWrapping(False)
        self.autoLogoutTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.autoLogoutTimeEdit.setCurrentSection(QDateTimeEdit.Section.MinuteSection)

        self.horizontalLayout_10.addWidget(self.autoLogoutTimeEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.autoLogoutCheckBox = QCheckBox(self.frame_9)
        self.autoLogoutCheckBox.setObjectName(u"autoLogoutCheckBox")

        self.horizontalLayout_10.addWidget(self.autoLogoutCheckBox)


        self.verticalLayout_15.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.autoLogoutFrame)

        self.autoHideDetailsFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.autoHideDetailsFrame.setObjectName(u"autoHideDetailsFrame")
        self.autoHideDetailsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.autoHideDetailsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.autoHideDetailsFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.autoHideDetailsFrame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_17.addWidget(self.label_12)

        self.frame_11 = QFrame(self.autoHideDetailsFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 5, 0, 5)
        self.line_7 = QFrame(self.frame_11)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_7)


        self.verticalLayout_17.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.autoHideDetailsFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(130, 0))
        self.label_13.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.autoHideDetailsTimeEdit = QTimeEdit(self.frame_12)
        self.autoHideDetailsTimeEdit.setObjectName(u"autoHideDetailsTimeEdit")
        self.autoHideDetailsTimeEdit.setWrapping(False)
        self.autoHideDetailsTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.autoHideDetailsTimeEdit.setCurrentSection(QDateTimeEdit.Section.MinuteSection)

        self.horizontalLayout_11.addWidget(self.autoHideDetailsTimeEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.autoHideDetailsCheckBox = QCheckBox(self.frame_12)
        self.autoHideDetailsCheckBox.setObjectName(u"autoHideDetailsCheckBox")

        self.horizontalLayout_11.addWidget(self.autoHideDetailsCheckBox)


        self.verticalLayout_17.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.autoHideDetailsFrame)

        self.backupFrame = QFrame(self.scrollAreaWidgetContents_2)
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
        self.backupTitleLabel.setFont(font1)
        self.backupTitleLabel.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.backupTitleLabel)

        self.frame_3 = QFrame(self.backupFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.autoBackupFrame = QFrame(self.backupFrame)
        self.autoBackupFrame.setObjectName(u"autoBackupFrame")
        self.autoBackupFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.autoBackupFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.autoBackupFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 4, 9, 4)
        self.label_4 = QLabel(self.autoBackupFrame)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        self.label_4.setFont(font3)
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
        self.horizontalLayout_3.setContentsMargins(9, 4, 9, 4)
        self.label_3 = QLabel(self.lastBackupFrame)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lastBackupLabel = QLabel(self.lastBackupFrame)
        self.lastBackupLabel.setObjectName(u"lastBackupLabel")

        self.horizontalLayout_3.addWidget(self.lastBackupLabel)


        self.verticalLayout_2.addWidget(self.lastBackupFrame)

        self.frame_14 = QFrame(self.backupFrame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_14)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 4, 9, 4)
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout_21.addWidget(self.label_18)

        self.backupPathFrame = QFrame(self.frame_14)
        self.backupPathFrame.setObjectName(u"backupPathFrame")
        self.backupPathFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.backupPathFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.backupPathFrame)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 4, 0, 4)
        self.backupPathLineEdit = QLineEdit(self.backupPathFrame)
        self.backupPathLineEdit.setObjectName(u"backupPathLineEdit")

        self.horizontalLayout_13.addWidget(self.backupPathLineEdit)

        self.btnClearBackupPathLineEdit = QPushButton(self.backupPathFrame)
        self.btnClearBackupPathLineEdit.setObjectName(u"btnClearBackupPathLineEdit")

        self.horizontalLayout_13.addWidget(self.btnClearBackupPathLineEdit)


        self.verticalLayout_21.addWidget(self.backupPathFrame)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.btnGetBackupPath = QPushButton(self.frame_15)
        self.btnGetBackupPath.setObjectName(u"btnGetBackupPath")
        self.btnGetBackupPath.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_14.addWidget(self.btnGetBackupPath)

        self.btnSetBackupPath = QPushButton(self.frame_15)
        self.btnSetBackupPath.setObjectName(u"btnSetBackupPath")
        self.btnSetBackupPath.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_14.addWidget(self.btnSetBackupPath)


        self.verticalLayout_21.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.backupDeleteFrame = QFrame(self.backupFrame)
        self.backupDeleteFrame.setObjectName(u"backupDeleteFrame")
        self.backupDeleteFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.backupDeleteFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.backupDeleteFrame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 4, -1, 4)
        self.backupDeleteBox = QComboBox(self.backupDeleteFrame)
        self.backupDeleteBox.setObjectName(u"backupDeleteBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backupDeleteBox.sizePolicy().hasHeightForWidth())
        self.backupDeleteBox.setSizePolicy(sizePolicy1)
        self.backupDeleteBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_15.addWidget(self.backupDeleteBox)

        self.btnDeleteBackup = QPushButton(self.backupDeleteFrame)
        self.btnDeleteBackup.setObjectName(u"btnDeleteBackup")
        self.btnDeleteBackup.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_15.addWidget(self.btnDeleteBackup)


        self.verticalLayout_2.addWidget(self.backupDeleteFrame)

        self.backupBtnFrame = QFrame(self.backupFrame)
        self.backupBtnFrame.setObjectName(u"backupBtnFrame")
        self.horizontalLayout = QHBoxLayout(self.backupBtnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 4, 9, 4)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.btnClearBackup = QPushButton(self.backupBtnFrame)
        self.btnClearBackup.setObjectName(u"btnClearBackup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnClearBackup.sizePolicy().hasHeightForWidth())
        self.btnClearBackup.setSizePolicy(sizePolicy2)
        self.btnClearBackup.setMinimumSize(QSize(100, 0))
        self.btnClearBackup.setStyleSheet(u"background: rgb(170, 0, 0);")

        self.horizontalLayout.addWidget(self.btnClearBackup)

        self.btnRestoreBackup = QPushButton(self.backupBtnFrame)
        self.btnRestoreBackup.setObjectName(u"btnRestoreBackup")
        self.btnRestoreBackup.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.btnRestoreBackup)

        self.btnCreateBackup = QPushButton(self.backupBtnFrame)
        self.btnCreateBackup.setObjectName(u"btnCreateBackup")
        self.btnCreateBackup.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.btnCreateBackup)


        self.verticalLayout_2.addWidget(self.backupBtnFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self.backupFrame)

        self.categoryFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.categoryFrame.setObjectName(u"categoryFrame")
        self.categoryFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.categoryFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.categoryFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.categpryTitleLabel = QLabel(self.categoryFrame)
        self.categpryTitleLabel.setObjectName(u"categpryTitleLabel")
        self.categpryTitleLabel.setFont(font1)
        self.categpryTitleLabel.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.categpryTitleLabel)

        self.frame_2 = QFrame(self.categoryFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.label_5 = QLabel(self.categoryFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.createCategoryFrame = QFrame(self.categoryFrame)
        self.createCategoryFrame.setObjectName(u"createCategoryFrame")
        self.createCategoryFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.createCategoryFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.createCategoryFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.createCategoryFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnCategpryColor = QPushButton(self.frame_4)
        self.btnCategpryColor.setObjectName(u"btnCategpryColor")
        self.btnCategpryColor.setMinimumSize(QSize(80, 20))

        self.horizontalLayout_4.addWidget(self.btnCategpryColor)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignRight)

        self.btnPreviewCatColor = QPushButton(self.frame_4)
        self.btnPreviewCatColor.setObjectName(u"btnPreviewCatColor")
        self.btnPreviewCatColor.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btnPreviewCatColor)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.createCategoryFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.categoryCreatLineEdit = QLineEdit(self.frame_5)
        self.categoryCreatLineEdit.setObjectName(u"categoryCreatLineEdit")
        self.categoryCreatLineEdit.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.categoryCreatLineEdit)

        self.btnCreateCategory = QPushButton(self.frame_5)
        self.btnCreateCategory.setObjectName(u"btnCreateCategory")
        self.btnCreateCategory.setMinimumSize(QSize(80, 20))

        self.horizontalLayout_6.addWidget(self.btnCreateCategory)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.createCategoryFrame)

        self.frame = QFrame(self.categoryFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 9, 2, 9)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: rgb(88, 88, 88);\n"
"padding:  5px 0px 5px 0px;")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_5.addWidget(self.line)


        self.verticalLayout_4.addWidget(self.frame)

        self.label_6 = QLabel(self.categoryFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6)

        self.editCategoryFrae = QFrame(self.categoryFrame)
        self.editCategoryFrae.setObjectName(u"editCategoryFrae")
        self.editCategoryFrae.setFrameShape(QFrame.Shape.NoFrame)
        self.editCategoryFrae.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.editCategoryFrae)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.editCategoryBox = QComboBox(self.editCategoryFrae)
        self.editCategoryBox.setObjectName(u"editCategoryBox")
        sizePolicy1.setHeightForWidth(self.editCategoryBox.sizePolicy().hasHeightForWidth())
        self.editCategoryBox.setSizePolicy(sizePolicy1)
        self.editCategoryBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.editCategoryBox)

        self.btnEditCategory = QPushButton(self.editCategoryFrae)
        self.btnEditCategory.setObjectName(u"btnEditCategory")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnEditCategory.sizePolicy().hasHeightForWidth())
        self.btnEditCategory.setSizePolicy(sizePolicy3)
        self.btnEditCategory.setMinimumSize(QSize(80, 15))

        self.horizontalLayout_5.addWidget(self.btnEditCategory, 0, Qt.AlignmentFlag.AlignVCenter)

        self.btnDeleteCategory = QPushButton(self.editCategoryFrae)
        self.btnDeleteCategory.setObjectName(u"btnDeleteCategory")
        sizePolicy3.setHeightForWidth(self.btnDeleteCategory.sizePolicy().hasHeightForWidth())
        self.btnDeleteCategory.setSizePolicy(sizePolicy3)
        self.btnDeleteCategory.setMinimumSize(QSize(80, 15))
        self.btnDeleteCategory.setStyleSheet(u"background: rgb(170, 0, 0);")

        self.horizontalLayout_5.addWidget(self.btnDeleteCategory, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.editCategoryFrae)


        self.verticalLayout_3.addWidget(self.categoryFrame)

        self.scrollAreaGeneral.setWidget(self.scrollAreaWidgetContents_2)

        self.vboxLayout1.addWidget(self.scrollAreaGeneral)

        self.stack.addWidget(self.page_general)
        self.page_security = QWidget()
        self.page_security.setObjectName(u"page_security")
        self.vboxLayout2 = QVBoxLayout(self.page_security)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.vboxLayout2.setContentsMargins(4, 4, 4, 4)
        self.securityTitle = QLabel(self.page_security)
        self.securityTitle.setObjectName(u"securityTitle")
        self.securityTitle.setFont(font)
        self.securityTitle.setStyleSheet(u"font: bold 14pt \"Segoe UI\";")
        self.securityTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.securityTitle)

        self.pw_frame = QFrame(self.page_security)
        self.pw_frame.setObjectName(u"pw_frame")
        self.pw_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_10 = QVBoxLayout(self.pw_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.pw_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_10.addWidget(self.label)

        self.frame_6 = QFrame(self.pw_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 5)
        self.line_4 = QFrame(self.frame_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.oldPwLabel = QLabel(self.pw_frame)
        self.oldPwLabel.setObjectName(u"oldPwLabel")

        self.verticalLayout_10.addWidget(self.oldPwLabel)

        self.old_pw = QLineEdit(self.pw_frame)
        self.old_pw.setObjectName(u"old_pw")
        self.old_pw.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_10.addWidget(self.old_pw)

        self.newPwLabel = QLabel(self.pw_frame)
        self.newPwLabel.setObjectName(u"newPwLabel")

        self.verticalLayout_10.addWidget(self.newPwLabel)

        self.new_pw1 = QLineEdit(self.pw_frame)
        self.new_pw1.setObjectName(u"new_pw1")
        self.new_pw1.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_10.addWidget(self.new_pw1)

        self.indicatorHolder = QVBoxLayout()
        self.indicatorHolder.setObjectName(u"indicatorHolder")

        self.verticalLayout_10.addLayout(self.indicatorHolder)

        self.repeatPwLabel = QLabel(self.pw_frame)
        self.repeatPwLabel.setObjectName(u"repeatPwLabel")

        self.verticalLayout_10.addWidget(self.repeatPwLabel)

        self.new_pw2 = QLineEdit(self.pw_frame)
        self.new_pw2.setObjectName(u"new_pw2")
        self.new_pw2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_10.addWidget(self.new_pw2)

        self.showPwCheckbox = QCheckBox(self.pw_frame)
        self.showPwCheckbox.setObjectName(u"showPwCheckbox")

        self.verticalLayout_10.addWidget(self.showPwCheckbox, 0, Qt.AlignmentFlag.AlignRight)

        self.btn_apply_pw = QPushButton(self.pw_frame)
        self.btn_apply_pw.setObjectName(u"btn_apply_pw")

        self.verticalLayout_10.addWidget(self.btn_apply_pw, 0, Qt.AlignmentFlag.AlignRight)


        self.vboxLayout2.addWidget(self.pw_frame)

        self.securitySpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout2.addItem(self.securitySpacer)

        self.stack.addWidget(self.page_security)
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.verticalLayout_13 = QVBoxLayout(self.page_import)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.importTitle = QLabel(self.page_import)
        self.importTitle.setObjectName(u"importTitle")
        self.importTitle.setFont(font)
        self.importTitle.setStyleSheet(u"font: bold 14pt \"Segoe UI\";")
        self.importTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.importTitle)

        self.importFrame = QFrame(self.page_import)
        self.importFrame.setObjectName(u"importFrame")
        self.importFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.importFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.importFrame)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.importFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_12.addWidget(self.label_8)

        self.frame_7 = QFrame(self.importFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 2, 0, 2)
        self.line_5 = QFrame(self.frame_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_5)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.importFrame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.importModeBox = QComboBox(self.importFrame)
        self.importModeBox.setObjectName(u"importModeBox")
        self.importModeBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.importModeBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.importFrame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.importFilePathLineEdit = QLineEdit(self.importFrame)
        self.importFilePathLineEdit.setObjectName(u"importFilePathLineEdit")

        self.horizontalLayout_8.addWidget(self.importFilePathLineEdit)

        self.btnSelectPath = QPushButton(self.importFrame)
        self.btnSelectPath.setObjectName(u"btnSelectPath")

        self.horizontalLayout_8.addWidget(self.btnSelectPath)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.progressFrame = QFrame(self.importFrame)
        self.progressFrame.setObjectName(u"progressFrame")
        self.progresslayout = QVBoxLayout(self.progressFrame)
        self.progresslayout.setSpacing(2)
        self.progresslayout.setObjectName(u"progresslayout")
        self.progresslayout.setContentsMargins(1, 1, 1, 1)
        self.progressLabel = QLabel(self.progressFrame)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progresslayout.addWidget(self.progressLabel)

        self.progressBar = QProgressBar(self.progressFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.progresslayout.addWidget(self.progressBar)


        self.verticalLayout_12.addWidget(self.progressFrame)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.btnStartImport = QPushButton(self.importFrame)
        self.btnStartImport.setObjectName(u"btnStartImport")

        self.horizontalLayout_9.addWidget(self.btnStartImport)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addWidget(self.importFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.stack.addWidget(self.page_import)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.verticalLayout_18 = QVBoxLayout(self.page_export)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.label_17 = QLabel(self.page_export)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: bold 14pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)

        self.frame_10 = QFrame(self.page_export)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setSpacing(12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"font: bold 10pt \"Segoe UI\";")

        self.verticalLayout_20.addWidget(self.label_16)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 2, 0, 2)
        self.line_8 = QFrame(self.frame_13)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background:rgb(170, 0, 0)")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_8)


        self.verticalLayout_20.addWidget(self.frame_13)

        self.exportFilenameLineEdit = QLineEdit(self.frame_10)
        self.exportFilenameLineEdit.setObjectName(u"exportFilenameLineEdit")

        self.verticalLayout_20.addWidget(self.exportFilenameLineEdit)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.exportFileLineEdit = QLineEdit(self.frame_10)
        self.exportFileLineEdit.setObjectName(u"exportFileLineEdit")

        self.horizontalLayout_12.addWidget(self.exportFileLineEdit)

        self.btnExportPath = QPushButton(self.frame_10)
        self.btnExportPath.setObjectName(u"btnExportPath")

        self.horizontalLayout_12.addWidget(self.btnExportPath)


        self.verticalLayout_20.addLayout(self.horizontalLayout_12)

        self.btnStartExport = QPushButton(self.frame_10)
        self.btnStartExport.setObjectName(u"btnStartExport")

        self.verticalLayout_20.addWidget(self.btnStartExport, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)

        self.stack.addWidget(self.page_export)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.vboxLayout3 = QVBoxLayout(self.page_about)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.vboxLayout3.setContentsMargins(4, 4, 4, 4)
        self.aboutTitle = QLabel(self.page_about)
        self.aboutTitle.setObjectName(u"aboutTitle")
        self.aboutTitle.setFont(font)
        self.aboutTitle.setStyleSheet(u"font: bold 14pt \"Segoe UI\";")
        self.aboutTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.aboutTitle, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.page_about)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 96, 26))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutLabel = QLabel(self.scrollAreaWidgetContents)
        self.aboutLabel.setObjectName(u"aboutLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.aboutLabel.sizePolicy().hasHeightForWidth())
        self.aboutLabel.setSizePolicy(sizePolicy4)
        self.aboutLabel.setTextFormat(Qt.TextFormat.RichText)
        self.aboutLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.aboutLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.aboutLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.vboxLayout3.addWidget(self.scrollArea)

        self.stack.addWidget(self.page_about)

        self.main_layout.addWidget(self.stack)


        self.retranslateUi(SettingsWindow)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.btn_general.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.btn_security.setText(QCoreApplication.translate("SettingsWindow", u"Security", None))
        self.btn_import.setText(QCoreApplication.translate("SettingsWindow", u"Import", None))
        self.btn_export.setText(QCoreApplication.translate("SettingsWindow", u"Export", None))
        self.btn_about.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.label_10.setText(QCoreApplication.translate("SettingsWindow", u"Auto. Logout", None))
        self.label_11.setText(QCoreApplication.translate("SettingsWindow", u"Logout Time (mm:ss):", None))
        self.autoLogoutTimeEdit.setDisplayFormat(QCoreApplication.translate("SettingsWindow", u"mm:ss", None))
        self.autoLogoutCheckBox.setText(QCoreApplication.translate("SettingsWindow", u"Active", None))
        self.label_12.setText(QCoreApplication.translate("SettingsWindow", u"Auto Hide Details", None))
        self.label_13.setText(QCoreApplication.translate("SettingsWindow", u"Hide Time (mm:ss):", None))
        self.autoHideDetailsTimeEdit.setDisplayFormat(QCoreApplication.translate("SettingsWindow", u"mm:ss", None))
        self.autoHideDetailsCheckBox.setText(QCoreApplication.translate("SettingsWindow", u"Active", None))
        self.backupTitleLabel.setText(QCoreApplication.translate("SettingsWindow", u"Backups", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Auto. Backups:", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Last Backup:", None))
        self.lastBackupLabel.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("SettingsWindow", u"Backup Path:", None))
        self.backupPathLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter a backup savepath ...", None))
        self.btnClearBackupPathLineEdit.setText("")
        self.btnGetBackupPath.setText(QCoreApplication.translate("SettingsWindow", u"Select Path", None))
        self.btnSetBackupPath.setText(QCoreApplication.translate("SettingsWindow", u"Set Path", None))
        self.backupDeleteBox.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Select a backup to delete...", None))
        self.btnDeleteBackup.setText(QCoreApplication.translate("SettingsWindow", u"Delete", None))
        self.btnClearBackup.setText(QCoreApplication.translate("SettingsWindow", u"Clear", None))
        self.btnRestoreBackup.setText(QCoreApplication.translate("SettingsWindow", u"Restore ", None))
        self.btnCreateBackup.setText(QCoreApplication.translate("SettingsWindow", u"Create ", None))
        self.categpryTitleLabel.setText(QCoreApplication.translate("SettingsWindow", u"Categories", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"Create new category.", None))
        self.btnCategpryColor.setText(QCoreApplication.translate("SettingsWindow", u"Pick Color", None))
        self.label_14.setText(QCoreApplication.translate("SettingsWindow", u"Preview:", None))
        self.btnPreviewCatColor.setText("")
        self.categoryCreatLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter category name...", None))
        self.btnCreateCategory.setText(QCoreApplication.translate("SettingsWindow", u"Create", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindow", u"Edit a category.", None))
        self.editCategoryBox.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Select a category...", None))
        self.btnEditCategory.setText(QCoreApplication.translate("SettingsWindow", u"Edit", None))
        self.btnDeleteCategory.setText(QCoreApplication.translate("SettingsWindow", u"Delete", None))
        self.securityTitle.setText(QCoreApplication.translate("SettingsWindow", u"Security", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Change Master Password", None))
        self.oldPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Password:", None))
        self.old_pw.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter current masterkey...", None))
        self.newPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"New Password:", None))
        self.new_pw1.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter new masterkey...", None))
        self.repeatPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Repeat New Password:", None))
        self.new_pw2.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Repeat new masterkey...", None))
        self.showPwCheckbox.setText(QCoreApplication.translate("SettingsWindow", u"Show", None))
        self.btn_apply_pw.setText(QCoreApplication.translate("SettingsWindow", u"Change Masterkey", None))
        self.importTitle.setText(QCoreApplication.translate("SettingsWindow", u"Import", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWindow", u"Import from File", None))
        self.label_7.setText(QCoreApplication.translate("SettingsWindow", u"Import Mode", None))
        self.importModeBox.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Select a mode...", None))
        self.label_9.setText(QCoreApplication.translate("SettingsWindow", u"Importfile", None))
        self.importFilePathLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter path to importfile...", None))
        self.btnSelectPath.setText(QCoreApplication.translate("SettingsWindow", u"Select File", None))
        self.progressLabel.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.btnStartImport.setText(QCoreApplication.translate("SettingsWindow", u"Start Import", None))
        self.label_17.setText(QCoreApplication.translate("SettingsWindow", u"Export", None))
        self.label_16.setText(QCoreApplication.translate("SettingsWindow", u"Export", None))
        self.exportFilenameLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter a filename to export...", None))
        self.label_15.setText(QCoreApplication.translate("SettingsWindow", u"Exportfile", None))
        self.exportFileLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter path to export directory...", None))
        self.btnExportPath.setText(QCoreApplication.translate("SettingsWindow", u"Select Path", None))
        self.btnStartExport.setText(QCoreApplication.translate("SettingsWindow", u"Start Export", None))
        self.aboutTitle.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.aboutLabel.setText(QCoreApplication.translate("SettingsWindow", u"PassTreasure v1.0", None))
    # retranslateUi

