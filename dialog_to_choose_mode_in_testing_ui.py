# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 279)
        self.btn_get_test = QtWidgets.QPushButton(Dialog)
        self.btn_get_test.setGeometry(QtCore.QRect(134, 90, 91, 23))
        self.btn_get_test.setObjectName("btn_get_test")
        self.btn_add_test = QtWidgets.QPushButton(Dialog)
        self.btn_add_test.setGeometry(QtCore.QRect(134, 130, 91, 23))
        self.btn_add_test.setObjectName("btn_add_test")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Тестирование: выбор режима"))
        self.btn_get_test.setText(_translate("Dialog", "Тестироваться"))
        self.btn_add_test.setText(_translate("Dialog", "Добавить тест"))

