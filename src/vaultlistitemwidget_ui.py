# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vaultlistitemwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_VaultListItemWidget(object):
    def setupUi(self, VaultListItemWidget):
        if not VaultListItemWidget.objectName():
            VaultListItemWidget.setObjectName(u"VaultListItemWidget")
        VaultListItemWidget.resize(300, 40)
        self.horizontalLayout = QHBoxLayout(VaultListItemWidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, -1, 11, -1)
        self.textLayout = QVBoxLayout()
        self.textLayout.setObjectName(u"textLayout")
        self.labelText = QLabel(VaultListItemWidget)
        self.labelText.setObjectName(u"labelText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelText.sizePolicy().hasHeightForWidth())
        self.labelText.setSizePolicy(sizePolicy)
        self.labelText.setStyleSheet(u"font-weight: bold; background: None;")
        self.labelText.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.textLayout.addWidget(self.labelText)


        self.horizontalLayout.addLayout(self.textLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.badgeLabel = QLabel(VaultListItemWidget)
        self.badgeLabel.setObjectName(u"badgeLabel")
        self.badgeLabel.setMinimumSize(QSize(60, 16))
        self.badgeLabel.setMaximumSize(QSize(60, 16))
        self.badgeLabel.setStyleSheet(u"font: 700 8pt \"Segoe UI\"; border-radius: 5px; background: rgba(211, 211, 211, 140);")
        self.badgeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.badgeLabel)


        self.retranslateUi(VaultListItemWidget)

        QMetaObject.connectSlotsByName(VaultListItemWidget)
    # setupUi

    def retranslateUi(self, VaultListItemWidget):
        self.labelText.setText(QCoreApplication.translate("VaultListItemWidget", u"1: Service (Username)", None))
        self.badgeLabel.setText(QCoreApplication.translate("VaultListItemWidget", u"General", None))
        pass
    # retranslateUi

