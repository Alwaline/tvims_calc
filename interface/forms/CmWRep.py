from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.py.cm_w_rep import Ui_Form
from interface.forms.Child import ChildForm

from service.calc import cm_w_rep


class CmWRepForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.formula.setPixmap(QPixmap("interface/images/6.png"))

    def calc(self):
        if self.k.text() and self.n.text():
            k = int(self.k.text())
            n = int(self.n.text())

            try:
                result = cm_w_rep(k, n)
                if int(result) == result:
                    self.result.setText(str(int(result)))
                else: self.result.setText(str(result))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))

    def clear_all(self):
        self.k.clear()
        self.n.clear()
        self.result.clear()
        self.k.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите k, n целыми числами. Требуется: k <= n")