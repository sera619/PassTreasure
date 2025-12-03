from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QApplication
from src.passwordgenerator_dialog_ui import Ui_PasswordGeneratorDialog
from backend.password_generator import PasswordGenerator
import resources_rc

class PasswordGeneratorPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PasswordGeneratorDialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/assets/icon.png"))
        self.ui.btnOkay.clicked.connect(self.accept)
        self.ui.btnGenerate.clicked.connect(self._generate_password)
        self.ui.btnCopy.clicked.connect(self._copy_password)
        self._password = ""
        
    
    def _generate_password(self):
        length = int(self.ui.spinLength.value())
        use_upper = self.ui.checkUpper.isChecked()
        use_numbers = self.ui.checkNumbers.isChecked()
        use_specials = self.ui.checkSpecial.isChecked()
        generator = PasswordGenerator(
            length=length,
            use_upper=use_upper,
            use_numbers=use_numbers,
            use_special=use_specials
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