import sys
from contact_with_base import DatabaseClass
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QLineEdit, QRadioButton, QCheckBox
from main_window_ui import Ui_MainWindow
from dialog_to_choose_mode_in_testing_ui import Ui_Dialog as Ui_choosing_dialog
from dialog_adding_task_ui import Ui_Dialog as Ui_adding_task
from warning_dialog_ui import Ui_Dialog as Ui_warning_dialog
from dialog_testing_ui import Ui_Dialog as Ui_dialog_testing
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

    def start_test(self):
        pass

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
                               'variants': self.variants, 'right_nums': self.numbers})
        else:
            database.add_task({"type": self.mode, 'task_text': self.plainTextEdit.toPlainText(),
                               'variants': self.lineEdit.text(), 'right_nums': None})
        open_warning_dialog(self, "Успешно!", "Вопрос добавлен в реестр!")

    def my_exit(self):
        super().close()


class DialogOnTesting(QDialog, Ui_dialog_testing):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.setupUi(self)
        self.btn_answer.clicked.connect(self.answer)
        self.counter_right = 0
        self.counter_all = 0
        self.n = 10
        self.data = database.data
        self.right_answer = None
        self.answer_inputs = []
        self.data = iter(shuffle(self.data)[:self.n])
        self.rewrite()
        self.now_mode = -1

    def answer(self):
        if self.now_mode == 1:
            

    def rewrite(self):
        self.progressBar.setValue(self.counter_all * (100 // self.n))
        self.lcd_all.display(self.counter_all)
        self.lcd_right.display(self.counter_right)
        working_task = next(self.data)
        mode = working_task['type']
        task_text = working_task['task_text']
        self.plainTextEdit.setPlainText(task_text)
        if mode == 1:
            self.answer_inputs = [QLineEdit(self)]
            self.answer_inputs[0].move(30, 200)
            self.right_answer = working_task['variants'][0]
        else:
            self.answer_inputs = []
            variants = working_task['variants']
            right_nums = working_task['right_nums']
            bar = len(variants)
            for x, y, text, indexx in zip_longest([30]*bar, range(200, 201+30*bar), variants, enumerate(1)):
                is_right = True if indexx in right_nums else False
                btn = MyQRadioButton(self, is_right) if mode == 2 else MyQCheckBox(self, is_right)
                if indexx == 1:
                    btn.setChecked(True)
                btn.move(x, y)
                btn.setText(text)
                self.answer_inputs.append(btn)
        self.now_mode = mode


class MyQRadioButton(QRadioButton):
    def __init__(self, parent, is_right):
        super().__init__(parent)
        self.is_right = is_right


class MyQCheckBox(QCheckBox):
    def __init__(self, parent, is_right):
        super().__init__(parent)
        self.is_right = is_right


def open_warning_dialog(parent, title, label_text):
    class WarningDialog(QDialog, Ui_warning_dialog):
        def __init__(self, parent, title, label_text):
            super().__init__(parent)
            self.setupUi(self)
            self.setWindowTitle(title)
            self.label.setText(label_text)
            self.label.resize(self.label.sizeHint())
            self.pushButton.clicked.connect(self.close)
            self.resize(500, 100)

    dialog = WarningDialog(parent, title, label_text)
    dialog.show()


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
    database.end()
    sys.exit(my_exit_code)
