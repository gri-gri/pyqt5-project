# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 388)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(110, 20, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 80, 211, 121))
        self.plainTextEdit.setUndoRedoEnabled(True)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_answer = QtWidgets.QPushButton(Dialog)
        self.btn_answer.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.btn_answer.setObjectName("btn_answer")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 250, 191, 88))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setText("")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.checkBox_2)
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup.addButton(self.checkBox_3)
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.buttonGroup.addButton(self.checkBox)
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup.addButton(self.checkBox_4)
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 90, 81, 92))
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 331, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Задание"))
        self.btn_answer.setText(_translate("Dialog", "Ответить"))
        self.label.setText(_translate("Dialog", "Правильно"))
        self.label_2.setText(_translate("Dialog", "из"))
        self.label_3.setText(_translate("Dialog", "Вопрос"))
        self.label_4.setText(_translate("Dialog", "Выберите один или несколько из предложенных ниже ответов"))

