from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.forms.Child import ChildForm
from interface.py.pl_w_rep import Ui_Form
from service.calc import pl_w_rep

class PlWRepForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.formula.setPixmap(QPixmap("interface/images/2.png"))


    def calc(self):
        if self.k.text() and self.n.text():
            k = int(self.k.text())
            n = int(self.n.text())

            try:
                self.result.setText(str(pl_w_rep(k, n)))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))

    def clear_all(self):
        self.k.clear()
        self.n.clear()
        self.result.clear()
        self.k.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите k, n целыми числами. Требуется: k <= n")