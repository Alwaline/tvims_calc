from abc import abstractmethod
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QWidget, QMessageBox

class ChildForm(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent: QWidget = parent

        self.back.clicked.connect(self.close)
        self.back.setShortcut(QKeySequence(Qt.Key.Key_Escape))
        self.calculate.clicked.connect(self.calc)
        self.calculate.setShortcut(QKeySequence(Qt.Key.Key_Return))
        self.clear.clicked.connect(self.clear_all)
        self.clear.setShortcut(QKeySequence("Ctrl+d"))
        self.help.clicked.connect(self.show_help)

    def close(self):
        self.parent.show()
        self.hide()
    
    @abstractmethod
    def calc(self):
        pass

    @abstractmethod
    def clear_all(self):
        pass

    @abstractmethod
    def show_help(self):
        pass

