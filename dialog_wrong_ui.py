# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(276, 212)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_next_question = QtWidgets.QPushButton(Dialog)
        self.btn_next_question.setGeometry(QtCore.QRect(50, 150, 121, 23))
        self.btn_next_question.setObjectName("btn_next_question")
        self.btn_judge = QtWidgets.QPushButton(Dialog)
        self.btn_judge.setGeometry(QtCore.QRect(180, 150, 75, 23))
        self.btn_judge.setObjectName("btn_judge")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Неверно!"))
        self.label.setText(_translate("Dialog", "Вы ответили неправильно!"))
        self.btn_next_question.setText(_translate("Dialog", "Следующий вопрос!"))
        self.btn_judge.setText(_translate("Dialog", "Оспорить!"))

