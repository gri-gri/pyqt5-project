# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(272, 184)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_next_question = QtWidgets.QPushButton(Dialog)
        self.btn_next_question.setGeometry(QtCore.QRect(130, 120, 121, 23))
        self.btn_next_question.setObjectName("btn_next_question")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Верно!"))
        self.label.setText(_translate("Dialog", "Вы ответили правильно!"))
        self.btn_next_question.setText(_translate("Dialog", "Следующий вопрос!"))

