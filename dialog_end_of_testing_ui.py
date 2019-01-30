# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_6.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(245, 190)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 151, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lcd_right = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_right.setObjectName("lcd_right")
        self.verticalLayout.addWidget(self.lcd_right)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lcd_all = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_all.setObjectName("lcd_all")
        self.verticalLayout.addWidget(self.lcd_all)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(160, 160, 41, 23))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Итог"))
        self.label.setText(_translate("Dialog", "Вы ответили правильно на "))
        self.label_2.setText(_translate("Dialog", "из"))
        self.label_3.setText(_translate("Dialog", "вопросов"))
        self.btn_ok.setText(_translate("Dialog", "OK"))

