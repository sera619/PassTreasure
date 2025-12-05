# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_edit_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CategoryEditDialog(object):
    def setupUi(self, CategoryEditDialog):
        if not CategoryEditDialog.objectName():
            CategoryEditDialog.setObjectName(u"CategoryEditDialog")
        CategoryEditDialog.resize(380, 180)
        CategoryEditDialog.setStyleSheet(u"    QPushButton {\n"
"        background-color: #2d2d30;\n"
"        border: 1px solid #3a3a3a;\n"
"        padding: 4px;\n"
"        border-radius: 6px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #3a3a3a;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #007acc;\n"
"        color: white;\n"
"    }")
        self.verticalLayout = QVBoxLayout(CategoryEditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameFrame = QFrame(CategoryEditDialog)
        self.nameFrame.setObjectName(u"nameFrame")
        self.nameRow = QHBoxLayout(self.nameFrame)
        self.nameRow.setObjectName(u"nameRow")
        self.label_name = QLabel(self.nameFrame)
        self.label_name.setObjectName(u"label_name")

        self.nameRow.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.nameFrame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.nameRow.addWidget(self.lineEdit_name)


        self.verticalLayout.addWidget(self.nameFrame)

        self.colorFrame = QFrame(CategoryEditDialog)
        self.colorFrame.setObjectName(u"colorFrame")
        self.colorRow = QHBoxLayout(self.colorFrame)
        self.colorRow.setObjectName(u"colorRow")
        self.label_color = QLabel(self.colorFrame)
        self.label_color.setObjectName(u"label_color")

        self.colorRow.addWidget(self.label_color)

        self.button_colorPreview = QPushButton(self.colorFrame)
        self.button_colorPreview.setObjectName(u"button_colorPreview")
        self.button_colorPreview.setMinimumSize(QSize(60, 25))
        self.button_colorPreview.setMaximumSize(QSize(40, 24))

        self.colorRow.addWidget(self.button_colorPreview)

        self.button_pickColor = QPushButton(self.colorFrame)
        self.button_pickColor.setObjectName(u"button_pickColor")

        self.colorRow.addWidget(self.button_pickColor)


        self.verticalLayout.addWidget(self.colorFrame)

        self.btnFrame = QFrame(CategoryEditDialog)
        self.btnFrame.setObjectName(u"btnFrame")
        self.buttonsRow = QHBoxLayout(self.btnFrame)
        self.buttonsRow.setObjectName(u"buttonsRow")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsRow.addItem(self.horizontalSpacer)

        self.button_save = QPushButton(self.btnFrame)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setMinimumSize(QSize(70, 0))

        self.buttonsRow.addWidget(self.button_save)

        self.button_cancel = QPushButton(self.btnFrame)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMinimumSize(QSize(70, 0))

        self.buttonsRow.addWidget(self.button_cancel)


        self.verticalLayout.addWidget(self.btnFrame)


        self.retranslateUi(CategoryEditDialog)

        QMetaObject.connectSlotsByName(CategoryEditDialog)
    # setupUi

    def retranslateUi(self, CategoryEditDialog):
        CategoryEditDialog.setWindowTitle(QCoreApplication.translate("CategoryEditDialog", u"Edit Category", None))
        self.label_name.setText(QCoreApplication.translate("CategoryEditDialog", u"Category Name:", None))
        self.label_color.setText(QCoreApplication.translate("CategoryEditDialog", u"Category Color:", None))
        self.button_colorPreview.setText("")
        self.button_pickColor.setText(QCoreApplication.translate("CategoryEditDialog", u"Pick Color", None))
        self.button_save.setText(QCoreApplication.translate("CategoryEditDialog", u"Save", None))
        self.button_cancel.setText(QCoreApplication.translate("CategoryEditDialog", u"Cancel", None))
    # retranslateUi

