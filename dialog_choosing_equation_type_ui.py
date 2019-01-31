# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_11.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(213, 126)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_square = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_square.setObjectName("btn_square")
        self.verticalLayout.addWidget(self.btn_square)
        self.btn_bisquare = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_bisquare.setObjectName("btn_bisquare")
        self.verticalLayout.addWidget(self.btn_bisquare)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Корни уравнений"))
        self.btn_square.setText(_translate("Dialog", "Квадратное"))
        self.btn_bisquare.setText(_translate("Dialog", "Биквадратное"))

