# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_text_dialog_popup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_GetTextDialogPopup(object):
    def setupUi(self, GetTextDialogPopup):
        if not GetTextDialogPopup.objectName():
            GetTextDialogPopup.setObjectName(u"GetTextDialogPopup")
        GetTextDialogPopup.resize(300, 180)
        self.verticalLayout_2 = QVBoxLayout(GetTextDialogPopup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.frame = QFrame(GetTextDialogPopup)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.frame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.titleLabel)

        self.textLabel = QLabel(self.frame)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.textLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.textLabel)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btnClearLineEdit = QPushButton(self.frame_2)
        self.btnClearLineEdit.setObjectName(u"btnClearLineEdit")

        self.horizontalLayout.addWidget(self.btnClearLineEdit)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(GetTextDialogPopup)
        self.buttonBox.accepted.connect(GetTextDialogPopup.accept)
        self.buttonBox.rejected.connect(GetTextDialogPopup.reject)

        QMetaObject.connectSlotsByName(GetTextDialogPopup)
    # setupUi

    def retranslateUi(self, GetTextDialogPopup):
        GetTextDialogPopup.setWindowTitle(QCoreApplication.translate("GetTextDialogPopup", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("GetTextDialogPopup", u"Title", None))
        self.textLabel.setText(QCoreApplication.translate("GetTextDialogPopup", u"Infotext", None))
        self.btnClearLineEdit.setText("")
    # retranslateUi

