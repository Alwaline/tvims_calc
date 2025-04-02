from PyQt6.QtWidgets import QApplication
from interface.forms.Main import MainForm
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm(app)
    
    window.show()
    app.exec()