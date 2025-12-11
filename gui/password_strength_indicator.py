from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QColor, QPainter
import config


class AnimatedDot(QWidget):
    def __init__(self, size=12, parent=None):
        super().__init__(parent)
        self.base_size = size
        self.current_color = QColor("#444")
        self.target_color = QColor("#444")
        
        self.setFixedSize(size, size)
        
        # Animations
        self.anim_opacity = QPropertyAnimation(self, b"windowOpacity")
        self.anim_opacity.setDuration(180)
        self.anim_opacity.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        self.anim_color = QPropertyAnimation(self, b"color")
        self.anim_color.setDuration(220)
        self.anim_color.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
    def _get_color(self):
        return self.current_color
        
    def _set_color(self, color):
        self.current_color = color
        self.update()  # Neuzeichnen
        
    color = Property(QColor, _get_color, _set_color)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Zeichne Kreis
        painter.setBrush(self.current_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.base_size, self.base_size)
        
        # Optional: Glow-Effekt
        # if self.current_color != QColor("#444"):
        #     painter.setBrush(Qt.BrushStyle.NoBrush)
        #     pen = QPen(self.current_color.lighter(150))
        #     pen.setWidth(2)
        #     painter.setPen(pen)
        #     painter.drawEllipse(1, 1, self.base_size-2, self.base_size-2)
        
    def activate(self, color: QColor):
        self.target_color = color
        
        # Fade opacity
        self.anim_opacity.stop()
        self.anim_opacity.setStartValue(0.6)
        self.anim_opacity.setEndValue(1.0)
        self.anim_opacity.start()
        
        # Color fade
        self.anim_color.stop()
        self.anim_color.setStartValue(self.current_color)
        self.anim_color.setEndValue(color)
        self.anim_color.start()
        
    def deactivate(self):
        grey = QColor("#444")
        self.target_color = grey
        
        # Fade opacity
        self.anim_opacity.stop()
        self.anim_opacity.setStartValue(1.0)
        self.anim_opacity.setEndValue(0.6)
        self.anim_opacity.start()
        
        # Color fade
        self.anim_color.stop()
        self.anim_color.setStartValue(self.current_color)
        self.anim_color.setEndValue(grey)
        self.anim_color.start()


class PasswordStrengthIndicator(QWidget):
    COLORS = [
        "#ff2e2e",
        "#ff6a00",
        "#ffcc00",
        "#9acd32",
        "#00cc44"
    ]

    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dots = []
        self.info_messages = config.TextStorage.PW_INDICATOR_STRENGTH_TEXTS
        
        layout = QHBoxLayout(self)
        layout.setSpacing(6)
        layout.setContentsMargins(8, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignVCenter)   # <— wichtig
        
        # dots
        dot_layout = QHBoxLayout()
        dot_layout.setSpacing(2)
        dot_layout.setContentsMargins(0, 2, 0, 0)
        dot_layout.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignVCenter)

        for _ in range(5):
            dot = AnimatedDot()
            self.dots.append(dot)
            dot_layout.addWidget(dot)

        # container für die dots → bekommt eine Mindesthöhe
        dot_container = QWidget()
        dot_container.setMinimumHeight(16)
        dot_container.setLayout(dot_layout)

        layout.addWidget(dot_container)
        
        # label
        self.label = QLabel()
        self.label.setStyleSheet("""font: 8pt "Segoe UI";""")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.label)

        # rechts ein Spacer, nicht links
        # layout.addStretch(-1)

    
    
    def set_strength(self, level: int):
        for i, dot in enumerate(self.dots):
            if i < level:
                self.label.setText(self.info_messages[level - 1])
                self.label.setStyleSheet(f"""font: 8pt "Segoe UI"; color:{self.COLORS[level - 1]};""")
                dot.activate(QColor(self.COLORS[level - 1]))
            else:
                dot.deactivate()