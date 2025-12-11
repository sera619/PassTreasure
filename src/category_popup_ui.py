# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_popup.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CategoryPopup(object):
    def setupUi(self, CategoryPopup):
        if not CategoryPopup.objectName():
            CategoryPopup.setObjectName(u"CategoryPopup")
        CategoryPopup.resize(286, 153)
        self.verticalLayout = QVBoxLayout(CategoryPopup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CategoryPopup)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBoxCategory = QComboBox(self.frame)
        self.comboBoxCategory.setObjectName(u"comboBoxCategory")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.comboBoxCategory)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnFrame = QFrame(self.frame)
        self.btnFrame.setObjectName(u"btnFrame")
        self.horizontalLayout = QHBoxLayout(self.btnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOK = QPushButton(self.btnFrame)
        self.btnOK.setObjectName(u"btnOK")

        self.horizontalLayout.addWidget(self.btnOK)

        self.btnCancel = QPushButton(self.btnFrame)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout_2.addWidget(self.btnFrame)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(CategoryPopup)

        QMetaObject.connectSlotsByName(CategoryPopup)
    # setupUi

    def retranslateUi(self, CategoryPopup):
        CategoryPopup.setWindowTitle(QCoreApplication.translate("CategoryPopup", u"PassTreasure - Change Category", None))
        self.label.setText(QCoreApplication.translate("CategoryPopup", u"Choose a category.", None))
        self.comboBoxCategory.setPlaceholderText(QCoreApplication.translate("CategoryPopup", u"Select a category...", None))
        self.btnOK.setText(QCoreApplication.translate("CategoryPopup", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("CategoryPopup", u"Cancel", None))
    # retranslateUi

