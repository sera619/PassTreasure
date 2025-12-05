from PySide6.QtCore import QObject, QEvent, QTimer, Signal

class InactivityWatcher(QObject):
    user_active = Signal()
    
    def eventFilter(self, obj, event: QEvent):
        if event.type() in (
            QEvent.Type.MouseMove,
            QEvent.Type.MouseButtonPress,
            QEvent.Type.KeyPress,
            QEvent.Type.Wheel,
            QEvent.Type.TouchBegin,
            QEvent.Type.FocusIn
        ):
            self.user_active.emit()
        return super().eventFilter(obj, event)

class AutoLocker(QObject):
    def __init__(self, timeout_ms: int, lock_callback):
        super().__init__()
        self.timeout_ms = timeout_ms
        self.lock_callback = lock_callback
        
        self.timer = QTimer()
        self.timer.setInterval(timeout_ms)
        self.timer.timeout.connect(self.lock_callback)
        self.timer.start()
    
    def reset(self):
        self.timer.start()