from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from interface.forms.Child import ChildForm
from interface.py.pr_wo_rep import Ui_Form
from service.calc import pr_wo_rep

class PrWoRepForm(ChildForm, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.formula.setPixmap(QPixmap("interface/images/3.png"))

    def calc(self):
        if self.n.text():
            n = int(self.n.text())

            try:
                self.result.setText(str(pr_wo_rep(n)))
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", str(e))

    def clear_all(self):
        self.n.clear()
        self.result.clear()
        self.n.setFocus()

    def show_help(self):
        QMessageBox.information(self, "Помощь", "Введите n целым числом")