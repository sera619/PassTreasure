from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter, QColor, QFont, QPen
from PySide6.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QTimer, QRectF, Signal
)
from src.splash_window_ui import Ui_SplashWindow
import resources_rc



class IntroSplash(QWidget):
    intro_finished = Signal()

    def __init__(self, animation_duration: int = 3500, delay_duration: int = 1500):
        super().__init__()
        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)

        # Frameless & transparent
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.SplashScreen)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Load logo
        self.logo = QPixmap(":/assets/icon.png")
        self.logo = self.logo.scaled(150, 150)
        self.ui.label_logo.setPixmap(self.logo)

        self.ui.label_text.setText("Loading PassTreasure...")

        # Animation control
        self.animation_duration = animation_duration
        self.delay_duration = delay_duration
        self._angle = 0

        # Loader timer
        self.loader_timer = QTimer(self)
        self.loader_timer.setInterval(16)
        self.loader_timer.timeout.connect(self._update_loader)

        self.setWindowOpacity(0.0)

        # Fade animation
        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setDuration(self.animation_duration)
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.fade_anim.finished.connect(self._on_fade_finished)
        self.server_process = None


    def _on_fade_finished(self):
        QTimer.singleShot(self.delay_duration, self.intro_finished.emit)
        
    def start(self):
        self.loader_timer.start()
        QTimer.singleShot(10, self.fade_anim.start)

    def _update_loader(self):
        self._angle = (self._angle + 5) % 360
        self.update()

    def paintEvent(self, event):
        """
        Draw custom loader arc.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Example arc around the bottom of the UI or anywhere you want
        rect = QRectF(self.width() / 2 - 20, self.height() - 80, 40, 40)

        pen = QPen(QColor(255, 255, 255, 180), 3)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        start = self._angle * 16
        span = 140 * 16

        painter.drawArc(rect, start, span)