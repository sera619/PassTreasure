# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_url_dialog.ui'
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

class Ui_EditUrlDialog(object):
    def setupUi(self, EditUrlDialog):
        if not EditUrlDialog.objectName():
            EditUrlDialog.setObjectName(u"EditUrlDialog")
        EditUrlDialog.resize(375, 214)
        self.verticalLayout_2 = QVBoxLayout(EditUrlDialog)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(EditUrlDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font:  bold 10pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label)

        self.serviceLabel = QLabel(self.frame)
        self.serviceLabel.setObjectName(u"serviceLabel")
        self.serviceLabel.setStyleSheet(u"color: rgb(184, 134, 11);\n"
"font: 600 italic 9pt \"Segoe UI\";")
        self.serviceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.serviceLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: bold 9pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.label_2)

        self.oldURLLabel = QLabel(self.frame)
        self.oldURLLabel.setObjectName(u"oldURLLabel")
        self.oldURLLabel.setStyleSheet(u"color: rgb(184, 134, 11);\n"
"font: 600 italic 9pt \"Segoe UI\";")
        self.oldURLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.oldURLLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.oldURLLabel)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 4, -1, 4)
        self.newUrlLineEdit = QLineEdit(self.frame)
        self.newUrlLineEdit.setObjectName(u"newUrlLineEdit")

        self.horizontalLayout.addWidget(self.newUrlLineEdit)

        self.btnClearuURL = QPushButton(self.frame)
        self.btnClearuURL.setObjectName(u"btnClearuURL")

        self.horizontalLayout.addWidget(self.btnClearuURL)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(EditUrlDialog)
        self.buttonBox.accepted.connect(EditUrlDialog.accept)
        self.buttonBox.rejected.connect(EditUrlDialog.reject)

        QMetaObject.connectSlotsByName(EditUrlDialog)
    # setupUi

    def retranslateUi(self, EditUrlDialog):
        EditUrlDialog.setWindowTitle(QCoreApplication.translate("EditUrlDialog", u"PassTreasure - Edit URL", None))
        self.label.setText(QCoreApplication.translate("EditUrlDialog", u"Edit URL for the service:", None))
        self.serviceLabel.setText(QCoreApplication.translate("EditUrlDialog", u"Servicename", None))
        self.label_2.setText(QCoreApplication.translate("EditUrlDialog", u"Current url:", None))
        self.oldURLLabel.setText(QCoreApplication.translate("EditUrlDialog", u"TextLabel", None))
        self.newUrlLineEdit.setPlaceholderText(QCoreApplication.translate("EditUrlDialog", u"Enter new url...", None))
        self.btnClearuURL.setText("")
    # retranslateUi

