# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_note_dialog.ui'
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
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_EditNoteDialog(object):
    def setupUi(self, EditNoteDialog):
        if not EditNoteDialog.objectName():
            EditNoteDialog.setObjectName(u"EditNoteDialog")
        EditNoteDialog.resize(375, 300)
        self.verticalLayout_2 = QVBoxLayout(EditNoteDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(EditNoteDialog)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.noteTextEdit = QTextEdit(self.frame)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteTextEdit.sizePolicy().hasHeightForWidth())
        self.noteTextEdit.setSizePolicy(sizePolicy)
        self.noteTextEdit.setStyleSheet(u"QTextEdit,\n"
"QTextEdit:focus,\n"
"QTextEdit:selected {\n"
"  	border: none;\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"  	border-bottom: 2px solid rgb(179, 179, 179);\n"
"  	background: transparent;\n"
"  	color: #fff;\n"
"  	padding: 5px 4px 4px 4px;\n"
"}\n"
"QTextEdit:focus {\n"
"  border: none;\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	background-color: rgb(38, 38, 38); \n"
"  border-bottom: 2px solid #42A5F5;\n"
"  color: #fff;\n"
"  padding: 5px 4px 4px 4px;\n"
"}\n"
"QTextEdit:disabled {\n"
"  border: none;\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"border-bottom:  none;\n"
" background-color: transparent; \n"
"  color: #000000;\n"
"  padding: 5px 4px 4px 4px;\n"
"}")
        self.noteTextEdit.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.noteTextEdit)

        self.btnCleatNote = QPushButton(self.frame)
        self.btnCleatNote.setObjectName(u"btnCleatNote")

        self.horizontalLayout.addWidget(self.btnCleatNote, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(EditNoteDialog)
        self.buttonBox.accepted.connect(EditNoteDialog.accept)
        self.buttonBox.rejected.connect(EditNoteDialog.reject)

        QMetaObject.connectSlotsByName(EditNoteDialog)
    # setupUi

    def retranslateUi(self, EditNoteDialog):
        EditNoteDialog.setWindowTitle(QCoreApplication.translate("EditNoteDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EditNoteDialog", u"Edit note for service:", None))
        self.serviceLabel.setText(QCoreApplication.translate("EditNoteDialog", u"Servicename", None))
        self.noteTextEdit.setPlaceholderText(QCoreApplication.translate("EditNoteDialog", u"Enter a note for the service...", None))
        self.btnCleatNote.setText("")
    # retranslateUi

