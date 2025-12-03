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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CategoryPopup(object):
    def setupUi(self, CategoryPopup):
        if not CategoryPopup.objectName():
            CategoryPopup.setObjectName(u"CategoryPopup")
        CategoryPopup.resize(241, 131)
        self.verticalLayout = QVBoxLayout(CategoryPopup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CategoryPopup)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBoxCategory = QComboBox(CategoryPopup)
        self.comboBoxCategory.setObjectName(u"comboBoxCategory")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.comboBoxCategory)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnOK = QPushButton(CategoryPopup)
        self.btnOK.setObjectName(u"btnOK")

        self.horizontalLayout.addWidget(self.btnOK)

        self.btnCancel = QPushButton(CategoryPopup)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CategoryPopup)

        QMetaObject.connectSlotsByName(CategoryPopup)
    # setupUi

    def retranslateUi(self, CategoryPopup):
        CategoryPopup.setWindowTitle(QCoreApplication.translate("CategoryPopup", u"Kategorie w\u00e4hlen", None))
        self.label.setText(QCoreApplication.translate("CategoryPopup", u"W\u00e4hle eine Kategorie:", None))
        self.comboBoxCategory.setPlaceholderText(QCoreApplication.translate("CategoryPopup", u"select category", None))
        self.btnOK.setText(QCoreApplication.translate("CategoryPopup", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("CategoryPopup", u"Abbrechen", None))
    # retranslateUi

