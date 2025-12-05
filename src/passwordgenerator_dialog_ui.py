# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordgenerator_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_PasswordGeneratorDialog(object):
    def setupUi(self, PasswordGeneratorDialog):
        if not PasswordGeneratorDialog.objectName():
            PasswordGeneratorDialog.setObjectName(u"PasswordGeneratorDialog")
        PasswordGeneratorDialog.resize(291, 245)
        self.verticalLayout = QVBoxLayout(PasswordGeneratorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PasswordGeneratorDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelLength = QLabel(PasswordGeneratorDialog)
        self.labelLength.setObjectName(u"labelLength")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLength)

        self.spinLength = QSpinBox(PasswordGeneratorDialog)
        self.spinLength.setObjectName(u"spinLength")
        self.spinLength.setMinimum(4)
        self.spinLength.setMaximum(64)
        self.spinLength.setValue(12)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinLength)

        self.labelOptions = QLabel(PasswordGeneratorDialog)
        self.labelOptions.setObjectName(u"labelOptions")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelOptions)

        self.optionsLayout = QVBoxLayout()
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.checkUpper = QCheckBox(PasswordGeneratorDialog)
        self.checkUpper.setObjectName(u"checkUpper")
        self.checkUpper.setChecked(True)

        self.optionsLayout.addWidget(self.checkUpper)

        self.checkNumbers = QCheckBox(PasswordGeneratorDialog)
        self.checkNumbers.setObjectName(u"checkNumbers")
        self.checkNumbers.setChecked(True)

        self.optionsLayout.addWidget(self.checkNumbers)

        self.checkSpecial = QCheckBox(PasswordGeneratorDialog)
        self.checkSpecial.setObjectName(u"checkSpecial")
        self.checkSpecial.setChecked(True)

        self.optionsLayout.addWidget(self.checkSpecial)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.optionsLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.lineGenerated = QLineEdit(PasswordGeneratorDialog)
        self.lineGenerated.setObjectName(u"lineGenerated")
        self.lineGenerated.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineGenerated)

        self.indicatorHolder = QVBoxLayout()
        self.indicatorHolder.setObjectName(u"indicatorHolder")

        self.verticalLayout.addLayout(self.indicatorHolder)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnGenerate = QPushButton(PasswordGeneratorDialog)
        self.btnGenerate.setObjectName(u"btnGenerate")

        self.buttonLayout.addWidget(self.btnGenerate)

        self.btnCopy = QPushButton(PasswordGeneratorDialog)
        self.btnCopy.setObjectName(u"btnCopy")

        self.buttonLayout.addWidget(self.btnCopy)

        self.btnOkay = QPushButton(PasswordGeneratorDialog)
        self.btnOkay.setObjectName(u"btnOkay")

        self.buttonLayout.addWidget(self.btnOkay)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PasswordGeneratorDialog)

        QMetaObject.connectSlotsByName(PasswordGeneratorDialog)
    # setupUi

    def retranslateUi(self, PasswordGeneratorDialog):
        PasswordGeneratorDialog.setWindowTitle(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Generator", None))
        self.label.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Generator", None))
        self.labelLength.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Password Length:", None))
        self.labelOptions.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Options:", None))
        self.checkUpper.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Include Uppercase", None))
        self.checkNumbers.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Include Numbers", None))
        self.checkSpecial.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Include Special Characters", None))
        self.lineGenerated.setPlaceholderText(QCoreApplication.translate("PasswordGeneratorDialog", u"Generated Password", None))
        self.btnGenerate.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Generate", None))
        self.btnCopy.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Copy", None))
        self.btnOkay.setText(QCoreApplication.translate("PasswordGeneratorDialog", u"Okay", None))
    # retranslateUi

