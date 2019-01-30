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
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(276, 212)
        self.btn_next_question = QtWidgets.QPushButton(Dialog)
        self.btn_next_question.setGeometry(QtCore.QRect(50, 150, 121, 23))
        self.btn_next_question.setObjectName("btn_next_question")
        self.btn_judge = QtWidgets.QPushButton(Dialog)
        self.btn_judge.setGeometry(QtCore.QRect(180, 150, 75, 23))
        self.btn_judge.setObjectName("btn_judge")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 161, 94))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_users_answer = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_users_answer.setText("")
        self.label_users_answer.setObjectName("label_users_answer")
        self.verticalLayout.addWidget(self.label_users_answer)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_right_answer = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_right_answer.setText("")
        self.label_right_answer.setObjectName("label_right_answer")
        self.verticalLayout.addWidget(self.label_right_answer)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Неверно!"))
        self.btn_next_question.setText(_translate("Dialog", "Следующий вопрос"))
        self.btn_judge.setText(_translate("Dialog", "Оспорить!"))
        self.label.setText(_translate("Dialog", "Вы ответили неправильно!"))
        self.label_2.setText(_translate("Dialog", "Ваш ответ:"))
        self.label_4.setText(_translate("Dialog", "Правильный ответ:"))

