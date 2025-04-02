from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.py.all_marked import Ui_Form
from interface.forms.Child import ChildForm

from service.calc import all_marked

class AllMarkedForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.formula.setPixmap(QPixmap("interface/images/7.png"))

    def calc(self):
        if self.k.text().isdigit() and self.m.text().isdigit() and self.n.text().isdigit():
            k = int(self.k.text())
            m = int(self.m.text())
            n = int(self.n.text())
            
            try:
                result = all_marked(k, m, n)
                if int(result) == result:
                    self.result.setText(str(int(result)))
                else: self.result.setText(str(result))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))

    def clear_all(self):
        self.k.clear()
        self.m.clear()
        self.n.clear()
        self.result.clear()
        self.k.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите k, m, n целыми числами. Требуется: k < m <= n") 

