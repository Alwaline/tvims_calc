from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication

from interface.py.main import Ui_Form
from interface.forms.AllMarked import AllMarkedForm
from interface.forms.RMarked import NMarkedForm
from interface.forms.PlWoRep import PlWoRepForm
from interface.forms.PlWRep import PlWRepForm
from interface.forms.PrWoRep import PrWoRepForm
from interface.forms.PrWRep import PrWRepForm
from interface.forms.CmWoRep import CmWoRepForm
from interface.forms.CmWRep import CmWRepForm

class MainForm(Ui_Form, QWidget):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap("interface/images/1.png"))
        self.label_2.setPixmap(QPixmap("interface/images/2.png"))
        self.label_3.setPixmap(QPixmap("interface/images/3.png"))
        self.label_4.setPixmap(QPixmap("interface/images/4.png"))
        self.label_5.setPixmap(QPixmap("interface/images/5.png"))
        self.label_6.setPixmap(QPixmap("interface/images/6.png"))
        self.label_7.setPixmap(QPixmap("interface/images/7.png"))
        self.label_8.setPixmap(QPixmap("interface/images/8.png"))
        self.app: QApplication = app

        self.all_marked_form: QWidget = AllMarkedForm(self)
        self.cm_wo_rep_form: QWidget = CmWoRepForm(self)
        self.cm_w_rep_form: QWidget = CmWRepForm(self)
        self.pl_wo_rep_form: QWidget = PlWoRepForm(self)
        self.pl_w_rep_form: QWidget = PlWRepForm(self)
        self.pr_wo_rep_form: QWidget = PrWoRepForm(self)
        self.pr_w_rep_form: QWidget = PrWRepForm(self)
        self.r_marked_form: QWidget = NMarkedForm(self)

        self.pushButton.clicked.connect(lambda _, FORM=self.pl_wo_rep_form: self.open_form(FORM))
        self.pushButton_2.clicked.connect(lambda _, FORM=self.pl_w_rep_form: self.open_form(FORM))
        self.pushButton_3.clicked.connect(lambda _, FORM=self.pr_wo_rep_form: self.open_form(FORM))
        self.pushButton_4.clicked.connect(lambda _, FORM=self.pr_w_rep_form: self.open_form(FORM))
        self.pushButton_5.clicked.connect(lambda _, FORM=self.cm_wo_rep_form: self.open_form(FORM))
        self.pushButton_6.clicked.connect(lambda _, FORM=self.cm_w_rep_form: self.open_form(FORM))
        self.pushButton_7.clicked.connect(lambda _, FORM=self.all_marked_form: self.open_form(FORM))
        self.pushButton_8.clicked.connect(lambda _, FORM=self.r_marked_form: self.open_form(FORM))

    def open_form(self, form: QWidget):
        form.show()
        self.hide()
        

