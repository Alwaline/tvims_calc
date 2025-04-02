from abc import abstractmethod
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QWidget, QMessageBox

class ChildForm(QWidget):
    '''
    Класс дочернего окна с калькулятором.
    '''
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
        self.help.setShortcut(QKeySequence(Qt.Key.Key_F1))

    def close(self):
        '''
        Закрытие дочернего окна и возврат на главное окно.
        '''
        self.parent.show()
        self.hide()
    
    @abstractmethod
    def calc(self):
        '''
        Вычисление выражения
        '''
        pass

    @abstractmethod
    def clear_all(self):
        '''
        Очиска всех полей.
        '''
        pass

    @abstractmethod
    def show_help(self):
        '''
        Открытие справки.
        '''
        pass

