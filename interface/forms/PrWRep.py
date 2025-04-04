from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.forms.Child import ChildForm
from interface.py.pr_w_rep import Ui_Form
from service.calc import pr_w_rep

class PrWRepForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.formula.setPixmap(QPixmap("interface/images/4.png"))

    def calc(self):
        if self.n_k.text():
            n_k = tuple(map(int, self.n_k.text().split()))

            try:
                result = pr_w_rep(*n_k)
                if int(result) == result:
                    self.result.setText(str(int(result)))
                else: self.result.setText(str(result))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))

    def clear_all(self):
        self.n_k.clear()
        self.result.clear()
        self.n_k.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите n целым числом. Введите k целых чисел через пробел. Требуется: n > 0; sum(n_k) = n")