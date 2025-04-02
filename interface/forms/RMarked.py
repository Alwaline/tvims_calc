from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.forms.Child import ChildForm
from service.calc import r_marked
from interface.py.r_marked import Ui_Form


class NMarkedForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.formula.setPixmap(QPixmap("interface/images/8.png"))

    def calc(self):
        if self.r.text() and self.n.text() and self.k.text() and self.m.text():
            r = int(self.r.text())
            n = int(self.n.text())
            k = int(self.k.text())
            m = int(self.m.text())

            try:
                result = r_marked(r, k, m, n)
                if int(result) == result:
                    self.result.setText(str(int(result)))
                else: self.result.setText(str(result))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))
        

    def clear_all(self):
        self.r.clear()
        self.n.clear()
        self.k.clear()
        self.m.clear()
        self.result.clear()
        self.r.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите r, k, m, n целыми числами. Требуется: k < m; k - r <= n - m; m <= n")