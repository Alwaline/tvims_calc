# Form implementation generated from reading ui file 'interface/ui/pr_wo_rep.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 310)
        Form.setMinimumSize(QtCore.QSize(512, 310))
        Form.setMaximumSize(QtCore.QSize(512, 310))
        Form.setMouseTracking(False)
        self.formula = QtWidgets.QLabel(parent=Form)
        self.formula.setGeometry(QtCore.QRect(6, 6, 500, 100))
        self.formula.setMinimumSize(QtCore.QSize(500, 100))
        self.formula.setMaximumSize(QtCore.QSize(500, 100))
        self.formula.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.formula.setStyleSheet("border: 1px solid red;\n"
"")
        self.formula.setText("")
        self.formula.setScaledContents(False)
        self.formula.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formula.setObjectName("formula")
        self.back = QtWidgets.QPushButton(parent=Form)
        self.back.setGeometry(QtCore.QRect(6, 270, 88, 34))
        self.back.setObjectName("back")
        self.calculate = QtWidgets.QPushButton(parent=Form)
        self.calculate.setGeometry(QtCore.QRect(420, 270, 88, 34))
        self.calculate.setObjectName("calculate")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 120, 160, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.n = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.n.setObjectName("n")
        self.horizontalLayout_7.addWidget(self.n)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.result = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.result.setEnabled(True)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.horizontalLayout_9.addWidget(self.result)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.help = QtWidgets.QPushButton(parent=Form)
        self.help.setGeometry(QtCore.QRect(470, 120, 31, 31))
        self.help.setObjectName("help")
        self.clear = QtWidgets.QPushButton(parent=Form)
        self.clear.setGeometry(QtCore.QRect(330, 270, 88, 34))
        self.clear.setObjectName("clear")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Перестановки без повторений"))
        self.back.setText(_translate("Form", "Назад"))
        self.calculate.setText(_translate("Form", "Рассчитать"))
        self.label_8.setText(_translate("Form", "n:"))
        self.label_10.setText(_translate("Form", "P:"))
        self.help.setText(_translate("Form", "?"))
        self.clear.setText(_translate("Form", "Очистить"))
