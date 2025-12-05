# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if not SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        SplashWindow.resize(480, 330)
        self.verticalLayout = QVBoxLayout(SplashWindow)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_logo = QLabel(SplashWindow)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(150, 150))
        self.label_logo.setStyleSheet(u"background: none;\n"
"")
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_logo)

        self.label_text = QLabel(SplashWindow)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setStyleSheet(u"color: white; \n"
"font-size: 22px;\n"
"background:none;")
        self.label_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_text)

        self.loaderSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.loaderSpacer)


        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"SplashWindow", None))
        self.label_logo.setText("")
        self.label_text.setText(QCoreApplication.translate("SplashWindow", u"Loading PassTreasure...", None))
    # retranslateUi

