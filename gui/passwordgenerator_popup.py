from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout
from src.passwordgenerator_dialog_ui import Ui_PasswordGeneratorDialog
from backend.password_generator import PasswordGenerator
from gui.password_strength_indicator import PasswordStrengthIndicator
from backend.password_strength_logic import evaluate_password_strength
import resources_rc
from config import Styles

class PasswordGeneratorPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PasswordGeneratorDialog()
        self.ui.setupUi(self)
        self._apply_style()
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.ui.btnOkay.clicked.connect(self.accept)
        self.ui.btnGenerate.clicked.connect(self._generate_password)
        self.ui.btnCopy.clicked.connect(self._copy_password)
        self.strength_indicator = PasswordStrengthIndicator(self)
        self.ui.indicatorHolder.addWidget(self.strength_indicator)
        self.ui.lineGenerated.textChanged.connect(self._update_strength)
        self._password = ""
        
    def _apply_style(self):
        self.ui.btnCopy.setStyleSheet(Styles.yellow_button_outlined)
        self.ui.btnGenerate.setStyleSheet(Styles.green_button_outlined)
        self.ui.btnOkay.setStyleSheet(Styles.green_button)
    
    def _update_strength(self):
        pw = self.ui.lineGenerated.text()
        level = evaluate_password_strength(pw)
        self.strength_indicator.set_strength(level)
    
    def _generate_password(self):
        length = int(self.ui.spinLength.value())
        use_upper = self.ui.checkUpper.isChecked()
        use_numbers = self.ui.checkNumbers.isChecked()
        use_specials = self.ui.checkSpecial.isChecked()
        excluded_chars = self.ui.excludeCharsLineEdit.text().split(" ")
        generator = PasswordGenerator(
            length=length,
            use_upper=use_upper,
            use_numbers=use_numbers,
            use_special=use_specials,
            excluded_chars=excluded_chars
        )
        self._password = generator.generate()
        self.ui.lineGenerated.setText(self._password)
        
    def _copy_password(self):
        password = self.ui.lineGenerated.text()
        if password:
            clipboard = QApplication.clipboard()
            clipboard.setText(password)

    def get_password(self) -> str:
        """Return the last generated password"""
        return self._password