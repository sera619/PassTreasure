from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap, QPainter, QColor, QFont, QPen
from PySide6.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QTimer, QRectF, Signal
)
from config import resource_path
import resources_rc

class IntroSplash(QSplashScreen):
    intro_finished = Signal()
    def __init__(self, animation_duration: int = 3500, delay_duration: int = 1500):
        self.logo = QPixmap(resource_path("assets/icon.png"))
        self.animation_duration = animation_duration
        self.delay_duration = delay_duration
        width = self.logo.width()
        height = self.logo.height() + 150
        splash_pixmap = QPixmap(width, height)
        splash_pixmap.fill(Qt.GlobalColor.transparent)

        super().__init__(splash_pixmap)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        self.setWindowOpacity(0.0)

        self._angle = 0

        self.loader_timer = QTimer()
        self.loader_timer.setInterval(16)
        self.loader_timer.timeout.connect(self._update_loader)

        self.fade_anim = QPropertyAnimation(self, b"windowOpacity")
        self.fade_anim.setDuration(self.animation_duration)
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.fade_anim.finished.connect(self._on_animation_finished)

    def _on_animation_finished(self):
        QTimer.singleShot(self.delay_duration, self.intro_finished.emit)

    def start(self):
        self.loader_timer.start()
        QTimer.singleShot(10, self.fade_anim.start)

    def _update_loader(self):
        self._angle = (self._angle + 5) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        x_logo = (self.width() - self.logo.width()) // 2
        y_logo = 0
        painter.drawPixmap(x_logo, y_logo, self.logo)

        y_center = self.logo.height() + 20
        splash_width = self.width() - 100
        text = "Loading PassTreasure..."
        painter.setPen(QColor(255, 255, 255, 230))
        font = QFont()
        font.setPointSize(24)
        painter.setFont(font)
        
        text_height = painter.fontMetrics().height()
        text_rect = QRectF(0, y_center, splash_width, text_height)
        
        painter.drawText(
            text_rect, 
            Qt.AlignmentFlag.AlignCenter, 
            text
        )

        loader_size = 36
        loader_x = (splash_width - loader_size) // 2 
        
        loader_y = y_center + text_height + 20 
        
        pen = QPen(QColor(255, 255, 255, 180), 3)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        start = self._angle * 16
        span = 140 * 16

        painter.drawArc(QRectF(loader_x, loader_y, loader_size, loader_size),
                        start, span)