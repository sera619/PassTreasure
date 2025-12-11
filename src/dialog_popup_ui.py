# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_popup.ui'
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
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_DialogPopup(object):
    def setupUi(self, DialogPopup):
        if not DialogPopup.objectName():
            DialogPopup.setObjectName(u"DialogPopup")
        DialogPopup.resize(310, 180)
        self.verticalLayout_3 = QVBoxLayout(DialogPopup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.frame = QFrame(DialogPopup)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.iconFrame = QFrame(self.frame)
        self.iconFrame.setObjectName(u"iconFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.iconFrame)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 6, 9, 6)
        self.iconLabel = QLabel(self.iconFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setPixmap(QPixmap(u":/assets/info.png"))
        self.iconLabel.setScaledContents(False)
        self.iconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.iconLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.titleLabel = QLabel(self.iconFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setStyleSheet(u"font: bold 15pt \"Segoe UI\";")
        self.titleLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addWidget(self.iconFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, 0, 16, 0)
        self.textLabel = QLabel(self.frame)
        self.textLabel.setObjectName(u"textLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textLabel.sizePolicy().hasHeightForWidth())
        self.textLabel.setSizePolicy(sizePolicy1)
        self.textLabel.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.textLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.textLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.textLabel)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(DialogPopup)
        self.buttonBox.accepted.connect(DialogPopup.accept)
        self.buttonBox.rejected.connect(DialogPopup.reject)

        QMetaObject.connectSlotsByName(DialogPopup)
    # setupUi

    def retranslateUi(self, DialogPopup):
        DialogPopup.setWindowTitle(QCoreApplication.translate("DialogPopup", u"Dialog", None))
        self.iconLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("DialogPopup", u"Title", None))
        self.textLabel.setText(QCoreApplication.translate("DialogPopup", u"TextLabel", None))
    # retranslateUi

