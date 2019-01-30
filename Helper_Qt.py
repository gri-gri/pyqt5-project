import sys
from contact_with_base import DatabaseClass
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QLineEdit, QRadioButton, QCheckBox, QMessageBox
from main_window_ui import Ui_MainWindow
from dialog_to_choose_mode_in_testing_ui import Ui_Dialog as Ui_choosing_dialog
from dialog_adding_task_ui import Ui_Dialog as Ui_adding_task
from warning_dialog_ui import Ui_Dialog as Ui_warning_dialog
from dialog_testing_ui import Ui_Dialog as Ui_dialog_testing
from dialog_wrong_ui import Ui_Dialog as Ui_dialog_wrong
from dialog_end_of_testing_ui import Ui_Dialog as Ui_dialog_end_of_testing
from random import shuffle
from itertools import zip_longest


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.go_to_testing)

    def go_to_testing(self):
        test_mode_choosing_dialog = DialogOnChoosingTestingMode(self)
        test_mode_choosing_dialog.show()


class DialogOnChoosingTestingMode(QDialog, Ui_choosing_dialog):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.setupUi(self)
        self.btn_get_test.clicked.connect(self.start_test)
        self.btn_add_test.clicked.connect(self.add_test)

    def help_func(self):
        try:
            working_task = next(self.data)
            print(working_task)
            mode = working_task['type']
            task_text = working_task['task_text']

            td = DialogOnTesting(self, mode)
            td.btn_answer.clicked.connect(td.answer)
            td.plainTextEdit.setPlainText(task_text)
            td.progressBar.setValue(self.counter_all * (100 // self.n))
            td.lcd_all.display(self.counter_all)
            td.lcd_right.display(self.counter_right)

            if mode == 1:
                td.answer_inputs = [QLineEdit(td)]
                td.answer_inputs[0].move(30, 200)
                self.right_answer = working_task['variants'][0]

            elif mode == 2:
                variants = working_task['variants']
                index_of_right_one = working_task['right_nums'][0]
                self.sp_of_radiobuttons = []
                for i in range(len(variants)):
                    btn = QRadioButton(variants[i], td)
                    if i == 0:
                        btn.setChecked(True)
                    btn.move(30, 200 + 30 * i)
                    self.sp_of_radiobuttons.append((btn, True if i + 1 == index_of_right_one else False, i))
                    print(btn)
                    print(btn.geometry())
                    print(btn.parent)
                    print(self.sp_of_radiobuttons)

            else:  # mode == 3
                variants = working_task['variants']
                indexes_of_right_ones = working_task['right_nums']
                self.sp_of_checkboxes = []
                for i in range(len(variants)):
                    btn = QCheckBox(variants[i], td)
                    if i == 0:
                        btn.setChecked(True)
                    btn.move(30, 200 + 30 * i)
                    self.sp_of_checkboxes.append((btn, True if i + 1 == indexes_of_right_ones else False, i))

        except StopIteration:
            self.submit()

    def submit(self):
        dialog = DialogEndOfTesting(self, self.counter_right, self.counter_all)
        dialog.show()

    def start_test(self):

        self.n = 10
        self.data = database.data
        shuffle(self.data)
        self.data = iter(self.data[:self.n])
        self.counter_all = 0
        self.counter_right = 0

        self.help_func()


    def add_test(self):
        adding_task_dialog = DialogOnAddingTask(self)
        adding_task_dialog.show()


class DialogOnAddingTask(QDialog, Ui_adding_task):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.setupUi(self)
        self.btn_choose_task_type.clicked.connect(self.choose_task_type)
        self.btn_add_variant.clicked.connect(self.add_variant)
        self.btn_add_right_variant_number.clicked.connect(
            self.add_right_variant_number)
        self.btn_accept.clicked.connect(self.submit)
        self.btn_exit.clicked.connect(self.my_exit)
        self.variants = []
        self.mode = REGIMS["Выбор одного из предложенных вариантов"]
        self.numbers = []
        self.switch_to_multi_variant_mode()

    def choose_task_type(self):
        foo = self.mode
        i, okBtnPressed = QInputDialog.getItem(self,
                                               "Тип задания",
                                               "Выбирайте с умом!\n\nУчтите уже введённые данные по вопросу\n" +
                                               "при выборе типа задания, пожалуйста!\n\n" +
                                               "Выберите тип задания",
                                               REGIMS.keys(), 1, False)
        if okBtnPressed:
            self.mode = REGIMS[i]
        if self.mode == 1:
            self.switch_to_one_answer_mode()
        elif foo == 1 and self.mode != 1:
            self.switch_to_multi_variant_mode()
        self.rewrite()

    def switch_to_one_answer_mode(self):
        self.btn_add_right_variant_number.setVisible(False)
        self.label_4.setVisible(False)
        self.label_right_variants_numbers.setVisible(False)
        self.btn_add_variant.setVisible(False)
        self.label_3.setVisible(False)
        self.plainTextEdit_2.setVisible(False)
        self.label_5.setVisible(True)
        self.lineEdit.setVisible(True)
        self.resize(328, 471)

    def switch_to_multi_variant_mode(self):
        self.btn_add_right_variant_number.setVisible(True)
        self.label_4.setVisible(True)
        self.label_right_variants_numbers.setVisible(True)
        self.btn_add_variant.setVisible(True)
        self.label_3.setVisible(True)
        self.plainTextEdit_2.setVisible(True)
        self.label_5.setVisible(False)
        self.lineEdit.setVisible(False)
        self.resize(652, 471)

    def add_variant(self):
        if self.mode == 1:
            open_warning_dialog(self, 'Неверный тип задания',
                                "Выберите другой тип задания")
            return None
        if len(self.variants) == 4:
            i, okBtnPressed = QInputDialog.getText(
                self, "Слишком много вариантов", "Введённый далее вариант перезапишет последний!")
            if okBtnPressed:
                self.variants[-1] = i
        else:
            i, okBtnPressed = QInputDialog.getText(
                self, "Добавление варианта ответа", "Введите вариант ответа")
            if okBtnPressed:
                self.variants.append(i)
        self.rewrite()

    def add_right_variant_number(self):
        if self.mode == 1:
            open_warning_dialog(self, 'Неверный тип задания',
                                "Выберите другой тип задания")
            return None
        if self.mode == 2 and len(self.numbers) == 1:
            i, okBtnPressed = QInputDialog.getInt(
                self, "Правильный ответ", "Ввиду выбранного Вами типа задания,\n" +
                                          "введённый далее Вами номер правильного ответа\nперезапишет" +
                " уже существующий",
                1, 1, len(self.variants), 1)
        else:
            i, okBtnPressed = QInputDialog.getInt(
                self, "Правильный ответ", "Введите номер правильного ответа",
                1, 1, len(self.variants), 1)
        if okBtnPressed:
            if self.mode == 2:
                self.numbers = [i]
            else:
                self.numbers.append(i)
        self.numbers = sorted(list(set(self.numbers)))
        self.rewrite()

    def rewrite(self):
        self.label_task_type.setText(REGIMS_BACKWARDS[self.mode])
        self.label_task_type.resize(self.label_task_type.sizeHint())
        self.plainTextEdit_2.setPlainText('\n'.join(self.variants))
        self.label_right_variants_numbers.setText(", ".join(map(str, self.numbers)))
        self.label_right_variants_numbers.resize(self.label_right_variants_numbers.sizeHint())

    def submit(self):
        if self.mode != 1:
            database.add_task({"type": self.mode, 'task_text': self.plainTextEdit.toPlainText(),
                               'variants': self.variants.copy(), 'right_nums': self.numbers.copy()})
        else:
            database.add_task({"type": self.mode, 'task_text': self.plainTextEdit.toPlainText(),
                               'variants': self.lineEdit.text(), 'right_nums': None})
        database.obnov()
        open_warning_dialog(self, "Успешно!", "Вопрос добавлен в реестр!")

    def my_exit(self):
        super().close()


class DialogOnTesting(QDialog, Ui_dialog_testing):
    def __init__(self, parent, mode):
        self.parent = parent
        super().__init__(parent)
        self.setupUi(self)
        self.mode = mode
        self.show()

    def answer(self):
        class DialogOnWrong(QDialog, Ui_dialog_wrong):
            def __init__(self, parent, users_answer, right_answer):
                self.parent = parent
                super().__init__()
                self.setupUi(self)
                self.btn_next_question.clicked.connect(self.myexit)
                self.btn_judge.clicked.connect(self.judge)
                self.label_right_answer.setText(right_answer)
                self.label_users_answer.setText(users_answer)

            def judge(self):
                open_warning_dialog(self, "WIP", "Work in progress(")

            def myexit(self):
                super().close()

        self.parent.counter_all += 1
        if self.mode == 1:
            user_answer = self.answer_inputs[0].text()
            if user_answer == self.parent.right_answer:
                self.parent.counter_right += 1
                open_warning_dialog(self, 'Верно', "Вы правильно ответили на вопрос!")
            else:
                dialog = DialogOnWrong(self, user_answer, self.parent.right_answer)
                dialog.show()
        elif self.mode == 2:
            btn_checked = next(filter(lambda btn: btn[0].isChecked(), self.parent.sp_of_radiobuttons))
            sp = self.parent.sp_of_radiobuttons
            if sp[sp.index(btn_checked)][1]:
                self.parent.counter_right += 1
                open_warning_dialog(self, 'Верно', "Вы правильно ответили на вопрос!")
            else:
                dialog = DialogOnWrong(self, btn_checked[0].text(), next(filter(lambda btn: btn[1],
                                                                             self.parent.sp_of_radiobuttons))[0].text())
                dialog.show()
        else:  # self.mode == 3
            btns_checked = sorted(list(filter(lambda btn: btn[0].isChecked(), self.parent.sp_of_checkboxes)),
                                  key=lambda btn: btn[0].text())
            right_btns = sorted(list(filter(lambda btn: btn[1], self.parent.sp_of_checkboxes)),
                                key=lambda btn: btn[0].text())
            if btns_checked == right_btns:
                self.parent.counter_right += 1
                open_warning_dialog(self, 'Верно', "Вы правильно ответили на вопрос!")
            else:
                dialog = DialogOnWrong(self, 'Номер(а): ' + ', '.join(map(lambda btn: str(btn[2]), btns_checked)),
                                       'Номер(а): ' + ', '.join(map(lambda btn: str(btn[2]), right_btns)))
                dialog.show()
        super().close()
        self.parent.help_func()


class DialogEndOfTesting(QDialog, Ui_dialog_end_of_testing):
    def __init__(self, parent, right, al):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.myexit)
        self.lcd_all.display(al)
        self.lcd_right.display(right)

    def myexit(self):
        super().close()


class MyQRadioButton(QRadioButton):
    def __init__(self, parent, is_right, indexx):
        super().__init__()
        self.parent = parent
        self.indexx = indexx
        self.is_right = is_right

    def isRight(self):
        return self.is_right


class MyQCheckBox(QCheckBox):
    def __init__(self, parent, is_right, indexx):
        super().__init__()
        self.parent = parent
        self.is_right = is_right
        self.indexx = indexx

    def isRight(self):
        return self.is_right


def open_warning_dialog(parent, title, label_text):
    foo = QMessageBox.information(parent, title, label_text)

REGIMS = {"Ввод пользовательского ответа": 1,
          "Выбор одного из предложенных вариантов": 2,
          "Выбор нескольких из предложенных вариантов": 3}

REGIMS_BACKWARDS = {i[1]: i[0] for i in REGIMS.items()}

if __name__ == '__main__':
    database = DatabaseClass()
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    my_exit_code = app.exec()
    database.obnov()
    sys.exit(my_exit_code)
