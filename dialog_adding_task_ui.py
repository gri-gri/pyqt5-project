# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_7.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 343)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_choose_task_type = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_choose_task_type.setObjectName("btn_choose_task_type")
        self.verticalLayout.addWidget(self.btn_choose_task_type)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_task_type = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_task_type.setText("")
        self.label_task_type.setObjectName("label_task_type")
        self.verticalLayout.addWidget(self.label_task_type)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(200, 20, 160, 92))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 120, 160, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_add_variant = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_add_variant.setEnabled(True)
        self.btn_add_variant.setObjectName("btn_add_variant")
        self.verticalLayout_3.addWidget(self.btn_add_variant)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.plainTextEdit_2.setEnabled(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_3.addWidget(self.plainTextEdit_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(200, 120, 200, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_add_right_variant_number = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_add_right_variant_number.setObjectName("btn_add_right_variant_number")
        self.verticalLayout_4.addWidget(self.btn_add_right_variant_number)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_right_variants_numbers = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_right_variants_numbers.setText("")
        self.label_right_variants_numbers.setObjectName("label_right_variants_numbers")
        self.verticalLayout_4.addWidget(self.label_right_variants_numbers)
        self.btn_accept = QtWidgets.QPushButton(Dialog)
        self.btn_accept.setGeometry(QtCore.QRect(260, 300, 81, 23))
        self.btn_accept.setObjectName("btn_accept")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление задания"))
        self.btn_choose_task_type.setText(_translate("Dialog", "Выбрать тип задания"))
        self.label.setText(_translate("Dialog", "Тип:"))
        self.label_2.setText(_translate("Dialog", "Введите текст задания:"))
        self.btn_add_variant.setText(_translate("Dialog", "Добавить вариант ответа"))
        self.label_3.setText(_translate("Dialog", "Варианты:"))
        self.btn_add_right_variant_number.setText(_translate("Dialog", "Добавить номер правильного ответа"))
        self.label_4.setText(_translate("Dialog", "Номера:"))
        self.btn_accept.setText(_translate("Dialog", "Подтвердить"))
