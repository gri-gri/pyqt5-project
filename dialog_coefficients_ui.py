# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_12.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(351, 264)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 291, 16))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 160, 86))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.get_a = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.get_a.setObjectName("get_a")
        self.gridLayout.addWidget(self.get_a, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.get_b = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.get_b.setObjectName("get_b")
        self.gridLayout.addWidget(self.get_b, 1, 1, 1, 1)
        self.get_c = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.get_c.setObjectName("get_c")
        self.gridLayout.addWidget(self.get_c, 2, 1, 1, 1)
        self.btn_calculate = QtWidgets.QPushButton(Dialog)
        self.btn_calculate.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.btn_calculate.setObjectName("btn_calculate")
        self.label_seem = QtWidgets.QLabel(Dialog)
        self.label_seem.setGeometry(QtCore.QRect(20, 40, 151, 16))
        self.label_seem.setText("")
        self.label_seem.setObjectName("label_seem")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 251, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Решение квадратного уравнения"))
        self.label.setText(_translate("Dialog", "Введите коэффициенты квадартного уравнения вида"))
        self.label_3.setText(_translate("Dialog", "b:"))
        self.label_4.setText(_translate("Dialog", "c:"))
        self.label_2.setText(_translate("Dialog", "a:"))
        self.btn_calculate.setText(_translate("Dialog", "Рассчитать"))
        self.label_5.setText(_translate("Dialog", "a, b и с можно представить в десятичном виде!"))

