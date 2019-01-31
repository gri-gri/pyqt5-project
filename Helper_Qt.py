import sys
from contact_with_base import DatabaseClass
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, \
QLineEdit, QRadioButton, QCheckBox, QMessageBox
from main_window_ui import Ui_MainWindow
from dialog_to_choose_mode_in_testing_ui import Ui_Dialog as Ui_choosing_dialog
from dialog_adding_task_ui import Ui_Dialog as Ui_adding_task
from dialog_testing_ui import Ui_Dialog as Ui_dialog_testing
from dialog_end_of_testing_ui import Ui_Dialog as Ui_dialog_end_of_testing
from dialog_label_ui import Ui_Dialog as Ui_dialog_label
from dialog_radiobutton_ui import Ui_Dialog as Ui_dialog_radiobutton_ui
from dialog_checkbox_ui import Ui_Dialog as Ui_dialog_checkbox_ui
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

    def add_test(self):
        adding_task_dialog = DialogOnAddingTask(self)
        adding_task_dialog.show()

    def start_test(self):
        self.N = 10
        self.data = database.data
        shuffle(self.data)
        self.data = iter(self.data[:self.N])
        self.counter_all = 0
        self.counter_right = 0
        self.set_next_question(next(self.data))

    def set_next_question(self, task_dct):
        if task_dct['mode'] == 1:
            self.now_working_dialog = DialogLabel(
                self, task_dct['task_text'],
                task_dct['correct_answer'],
                (100//self.N)*self.counter_all,
                self.counter_right, self.counter_all)
        elif task_dct['mode'] == 2:
            self.now_working_dialog = DialogRadiobutton(
                self, task_dct['task_text'],
                task_dct['index_of_correct_answer'],
                task_dct['variants'],
                (100 // self.N) * self.counter_all,
                self.counter_right, self.counter_all)
        else:  # task_dct['mode'] == 3
            self.now_working_dialog = DialogCheckbox(
                self, task_dct['task_text'],
                task_dct['indexes_of_correct_answers'],
                task_dct['variants'],
                (100 // self.N) * self.counter_all,
                self.counter_right, self.counter_all)

    def answer(self):
        try:
            self.counter_right, self.counter_all = \
                                self.now_working_dialog.answer()
            self.now_working_dialog.close()
            self.set_next_question(next(self.data))
        except StopIteration:
            self.submit()

    def submit(self):
        dialog = DialogEndOfTesting(self, self.counter_right, self.counter_all)
        dialog.show()


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
        i, okBtnPressed = \
           QInputDialog.getItem(self,
                                "Тип задания",
                                "Выбирайте с умом!" +
                                "\n\nУчтите уже введённые" +
                                " данные по вопросу\n" +
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
                self, "Слишком много вариантов",
                "Введённый далее вариант перезапишет последний!")
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
                self, "Правильный ответ",
                "Ввиду выбранного Вами типа задания,\n" +
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
        self.label_right_variants_numbers.setText(", ".join(map(str,
                                                                self.numbers)))
        self.label_right_variants_numbers.resize(
            self.label_right_variants_numbers.sizeHint())

    def submit(self):
        if self.mode == 1:
            database.add_task({"mode": 1, 'task_text':
                               self.plainTextEdit.toPlainText(),
                               'correct_answer': self.lineEdit.text()})
        elif self.mode == 2:
            database.add_task({"mode": 2, 'task_text':
                               self.plainTextEdit.toPlainText(),
                               'variants': self.variants.copy(),
                               'index_of_correct_answer':
                               self.numbers.copy()[0]})
        else:  # self.mode == 3
            database.add_task({"mode": 3, 'task_text':
                               self.plainTextEdit.toPlainText(),
                               'variants': self.variants.copy(),
                               'indexes_of_correct_answers': self.numbers.copy()})
        database.obnov()
        open_warning_dialog(self, "Успешно!", "Вопрос добавлен в реестр!")

    def my_exit(self):
        super().close()


class DialogLabel(QDialog, Ui_dialog_label):
    def __init__(self, parent, task_text,
                 right_answer, progress_bar_value, correct_value, all_value):
        super().__init__(parent)
        self.master = parent
        self.setupUi(self)
        self.plainTextEdit.setPlainText(task_text)
        self.correct_answer = right_answer
        self.progressBar.setValue(progress_bar_value)
        self.correct_value = correct_value
        self.all_value = all_value
        self.lcd_all.display(all_value)
        self.lcd_right.display(correct_value)
        self.btn_answer.clicked.connect(self.master.answer)
        self.show()

    def answer(self):
        self.all_value += 1
        users_answer = self.lineEdit.text()
        if users_answer == self.correct_answer:
            self.correct_value += 1
            open_warning_dialog(self, 'Верно',
                                "Вы правильно ответили на вопрос!")
        else:
            open_warning_dialog(self, 'Неверно',
                                "Неверно!\nВаш ответ:" +
                                "\n{}\nПравильный ответ:\n" +
                                "{}".format(users_answer
                                            if users_answer != '' else '-',
                                            self.correct_answer))
        return self.correct_value, self.all_value


class DialogRadiobutton(QDialog, Ui_dialog_radiobutton_ui):
    def __init__(self, parent, task_text, index_of_correct_answer, variants,
                 progress_bar_value, correct_value, all_value):
        super().__init__(parent)
        self.master = parent
        self.setupUi(self)
        self.plainTextEdit.setPlainText(task_text)
        self.progressBar.setValue(progress_bar_value)
        self.correct_value = correct_value
        self.all_value = all_value
        self.lcd_all.display(all_value)
        self.lcd_right.display(correct_value)
        self.btn_answer.clicked.connect(self.master.answer)
        self.btns = sorted(list(self.buttonGroup.buttons()),
                           key=lambda btn: btn.geometry().y())
        self.index_of_correct_answer = index_of_correct_answer
        for i in range(len(self.btns)):
            try:
                self.btns[i].setText(variants[i])
            except IndexError:
                self.btns[i].setVisible(False)
        self.show()

    def answer(self):
        self.all_value += 1
        users_answer = next(filter(lambda btn: btn.isChecked(), self.btns))
        if self.btns.index(users_answer) + 1 == self.index_of_correct_answer:
            self.correct_value += 1
            open_warning_dialog(self, 'Верно',
                                "Вы правильно ответили на вопрос!")
        else:
            open_warning_dialog(self, 'Неверно',
                                "Неверно!\nВы выбрали кнопку номер:" +
                                " {}\nПравильный ответ - кнопка номер" +
                                " {}".format(self.btns.index(users_answer),
                                             self.index_of_correct_answer + 1))
        return self.correct_value, self.all_value


class DialogCheckbox(QDialog, Ui_dialog_checkbox_ui):
    def __init__(self, parent, task_text, indexes_of_correct_answers,
                 variants, progress_bar_value, correct_value, all_value):
        super().__init__(parent)
        self.master = parent
        self.setupUi(self)
        self.plainTextEdit.setPlainText(task_text)
        self.progressBar.setValue(progress_bar_value)
        self.correct_value = correct_value
        self.all_value = all_value
        self.lcd_all.display(all_value)
        self.lcd_right.display(correct_value)
        self.btn_answer.clicked.connect(self.master.answer)
        self.btns = sorted(list(self.buttonGroup.buttons()),
                           key=lambda btn: btn.geometry().y())
        self.indexes_of_correct_answers = indexes_of_correct_answers
        for i in range(len(self.btns)):
            try:
                self.btns[i].setText(variants[i])
            except IndexError:
                self.btns[i].setVisible(False)
        self.show()

    def answer(self):
        self.all_value += 1
        users_answer = list(map(lambda btn: self.btns.index(btn) + 1, filter(lambda btn: btn.isChecked(), self.btns)))
        if users_answer == self.indexes_of_correct_answers:
            self.correct_value += 1
            open_warning_dialog(self, 'Верно',
                                "Вы правильно ответили на вопрос!")
        else:
            open_warning_dialog(self, 'Неверно',
                                "Неверно!\nВы выбрали кнопки номер:" +
                                "{}\nПравильный ответ - кнопки номер" +
                                " {}".format(
                                    ', '.join(map(str, users_answer))
                                    if ', '.join(map(str, users_answer)) != ''
                                    else '-',
                                    ', '.join(
                                        map(str,
                                            self.indexes_of_correct_answers))))
        return self.correct_value, self.all_value


class DialogEndOfTesting(QDialog, Ui_dialog_end_of_testing):
    def __init__(self, parent, right, al):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.myexit)
        self.lcd_all.display(al)
        self.lcd_right.display(right)

    def myexit(self):
        super().close()


def open_warning_dialog(parent, title, label_text):
    QMessageBox.information(parent, title, label_text)


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
