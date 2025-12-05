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
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.btn_general = QPushButton(self.sidebar)
        self.btn_general.setObjectName(u"btn_general")

        self.vboxLayout.addWidget(self.btn_general)

        self.btn_security = QPushButton(self.sidebar)
        self.btn_security.setObjectName(u"btn_security")

        self.vboxLayout.addWidget(self.btn_security)

        self.btn_import = QPushButton(self.sidebar)
        self.btn_import.setObjectName(u"btn_import")

        self.vboxLayout.addWidget(self.btn_import)

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

        self.scrollAreaGeneral = QScrollArea(self.page_general)
        self.scrollAreaGeneral.setObjectName(u"scrollAreaGeneral")
        self.scrollAreaGeneral.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaGeneral.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 473, 607))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setSpacing(40)
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
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_10.setFont(font1)

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

        self.horizontalLayout_10.addWidget(self.label_11)

        self.autoLogoutTimeEdit = QTimeEdit(self.frame_9)
        self.autoLogoutTimeEdit.setObjectName(u"autoLogoutTimeEdit")
        self.autoLogoutTimeEdit.setWrapping(False)
        self.autoLogoutTimeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.autoLogoutTimeEdit.setCurrentSection(QDateTimeEdit.Section.SecondSection)

        self.horizontalLayout_10.addWidget(self.autoLogoutTimeEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.autoLogoutCheckBox = QCheckBox(self.frame_9)
        self.autoLogoutCheckBox.setObjectName(u"autoLogoutCheckBox")

        self.horizontalLayout_10.addWidget(self.autoLogoutCheckBox)


        self.verticalLayout_15.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.autoLogoutFrame)

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
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.btnCreateBackup = QPushButton(self.backupBtnFrame)
        self.btnCreateBackup.setObjectName(u"btnCreateBackup")
        self.btnCreateBackup.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnCreateBackup)

        self.btnRestoreBackup = QPushButton(self.backupBtnFrame)
        self.btnRestoreBackup.setObjectName(u"btnRestoreBackup")
        self.btnRestoreBackup.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnRestoreBackup)

        self.btnDeleteBackup = QPushButton(self.backupBtnFrame)
        self.btnDeleteBackup.setObjectName(u"btnDeleteBackup")
        self.btnDeleteBackup.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnDeleteBackup)

        self.btnClearBackup = QPushButton(self.backupBtnFrame)
        self.btnClearBackup.setObjectName(u"btnClearBackup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnClearBackup.sizePolicy().hasHeightForWidth())
        self.btnClearBackup.setSizePolicy(sizePolicy1)
        self.btnClearBackup.setMinimumSize(QSize(80, 0))
        self.btnClearBackup.setStyleSheet(u"background: rgb(170, 0, 0);")

        self.horizontalLayout.addWidget(self.btnClearBackup)


        self.verticalLayout_2.addWidget(self.backupBtnFrame)


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

        self.createCategoryFrame = QFrame(self.categoryFrame)
        self.createCategoryFrame.setObjectName(u"createCategoryFrame")
        self.createCategoryFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.createCategoryFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.createCategoryFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.label_5 = QLabel(self.createCategoryFrame)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setBold(True)
        self.label_5.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_5)

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

        self.btnPreviewCatColor = QPushButton(self.frame_4)
        self.btnPreviewCatColor.setObjectName(u"btnPreviewCatColor")

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
        self.label_6.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_6)

        self.editCategoryFrae = QFrame(self.categoryFrame)
        self.editCategoryFrae.setObjectName(u"editCategoryFrae")
        self.editCategoryFrae.setFrameShape(QFrame.Shape.NoFrame)
        self.editCategoryFrae.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.editCategoryFrae)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.editCategoryBox = QComboBox(self.editCategoryFrae)
        self.editCategoryBox.setObjectName(u"editCategoryBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editCategoryBox.sizePolicy().hasHeightForWidth())
        self.editCategoryBox.setSizePolicy(sizePolicy2)
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
        self.securityTitle = QLabel(self.page_security)
        self.securityTitle.setObjectName(u"securityTitle")
        self.securityTitle.setFont(font)
        self.securityTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout2.addWidget(self.securityTitle)

        self.pw_frame = QFrame(self.page_security)
        self.pw_frame.setObjectName(u"pw_frame")
        self.pw_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_10 = QVBoxLayout(self.pw_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.pw_frame)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label.setFont(font5)

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
        self.importTitle = QLabel(self.page_import)
        self.importTitle.setObjectName(u"importTitle")
        self.importTitle.setFont(font1)
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
        self.label_8.setFont(font4)

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

        self.browserBox = QComboBox(self.importFrame)
        self.browserBox.setObjectName(u"browserBox")
        self.browserBox.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.browserBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.importFrame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.exportFilePathLineEdit = QLineEdit(self.importFrame)
        self.exportFilePathLineEdit.setObjectName(u"exportFilePathLineEdit")

        self.horizontalLayout_8.addWidget(self.exportFilePathLineEdit)

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
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.vboxLayout3 = QVBoxLayout(self.page_about)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.aboutTitle = QLabel(self.page_about)
        self.aboutTitle.setObjectName(u"aboutTitle")
        self.aboutTitle.setFont(font)
        self.aboutTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout3.addWidget(self.aboutTitle, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.page_about)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 481, 338))
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
        self.btn_about.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.label_10.setText(QCoreApplication.translate("SettingsWindow", u"Auto. Logout", None))
        self.label_11.setText(QCoreApplication.translate("SettingsWindow", u"Logout Time (mm:ss):", None))
        self.autoLogoutTimeEdit.setDisplayFormat(QCoreApplication.translate("SettingsWindow", u"mm:ss", None))
        self.autoLogoutCheckBox.setText(QCoreApplication.translate("SettingsWindow", u"Active", None))
        self.backupTitleLabel.setText(QCoreApplication.translate("SettingsWindow", u"Backups", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Auto. Backups:", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Last Backup:", None))
        self.backUpPathLabel.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.btnCreateBackup.setText(QCoreApplication.translate("SettingsWindow", u"Create ", None))
        self.btnRestoreBackup.setText(QCoreApplication.translate("SettingsWindow", u"Restore ", None))
        self.btnDeleteBackup.setText(QCoreApplication.translate("SettingsWindow", u"Delete", None))
        self.btnClearBackup.setText(QCoreApplication.translate("SettingsWindow", u"Clear", None))
        self.categpryTitleLabel.setText(QCoreApplication.translate("SettingsWindow", u"Categories", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"Create new category.", None))
        self.btnCategpryColor.setText(QCoreApplication.translate("SettingsWindow", u"Pick Color", None))
        self.btnPreviewCatColor.setText("")
        self.categoryCreatLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter category name...", None))
        self.btnCreateCategory.setText(QCoreApplication.translate("SettingsWindow", u"Create", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindow", u"Edit a category.", None))
        self.editCategoryBox.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Select a category...", None))
        self.btnEditCategory.setText(QCoreApplication.translate("SettingsWindow", u"Edit", None))
        self.btnDeleteCategory.setText(QCoreApplication.translate("SettingsWindow", u"Delete", None))
        self.securityTitle.setText(QCoreApplication.translate("SettingsWindow", u"Security", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Change Master Password", None))
        self.oldPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Old Password:", None))
        self.old_pw.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter current masterkey...", None))
        self.newPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"New Password:", None))
        self.new_pw1.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter new masterkey...", None))
        self.repeatPwLabel.setText(QCoreApplication.translate("SettingsWindow", u"Repeat Password:", None))
        self.new_pw2.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Repeat new masterkey...", None))
        self.showPwCheckbox.setText(QCoreApplication.translate("SettingsWindow", u"Show", None))
        self.btn_apply_pw.setText(QCoreApplication.translate("SettingsWindow", u"Apply Master Password", None))
        self.importTitle.setText(QCoreApplication.translate("SettingsWindow", u"Import", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWindow", u"Browser Imports", None))
        self.label_7.setText(QCoreApplication.translate("SettingsWindow", u"Browser:", None))
        self.browserBox.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Select a Browser...", None))
        self.label_9.setText(QCoreApplication.translate("SettingsWindow", u"Exportfile Path:", None))
        self.exportFilePathLineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"Enter path to exportfile...", None))
        self.btnSelectPath.setText(QCoreApplication.translate("SettingsWindow", u"Select Path", None))
        self.progressLabel.setText(QCoreApplication.translate("SettingsWindow", u"TextLabel", None))
        self.btnStartImport.setText(QCoreApplication.translate("SettingsWindow", u"Start Import", None))
        self.aboutTitle.setText(QCoreApplication.translate("SettingsWindow", u"About", None))
        self.aboutLabel.setText(QCoreApplication.translate("SettingsWindow", u"PassTreasure v1.0", None))
    # retranslateUi

