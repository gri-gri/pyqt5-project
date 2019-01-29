import sys
from contact_with_base import get_tasks, add_task
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog
from main_window_ui import Ui_MainWindow
from dialog_to_choose_mode_in_testing_ui import Ui_Dialog as Ui_choosing_dialog
from dialog_adding_task_ui import Ui_Dialog as Ui_adding_task
from warning_dialog_ui import Ui_Dialog as Ui_warning_dialog


def open_warning_dialog(parent, title, label_text):
    class WarningDialog(QDialog, Ui_warning_dialog):
        def __init__(self, parent, title, label_text):
            super().__init__(parent)
            self.setupUi(self)
            self.setTitle(title)
            self.label.setText(label_text)
            self.label.resize(self.label.sizeHint())
            self.pushButton.clicked.connect(self.close)
            
    dialog = WarningDialog(parent, title, label_text)
    dialog.show()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.go_to_testing)
        '''self.already_test_exists = False'''
        
    def go_to_testing(self):
        test_mode_choosing_dialog = DialogOnChoosingTestingMode(self)
        test_mode_choosing_dialog.show()
        
    '''
    def go_to_testing(self):
        if not self.already_test_exists:
            test_mode_choosing_dialog = DialogOnChoosingTestingMode(self)
            test_mode_choosing_dialog.show()
            self.already_test_exists = True
    '''
    
class DialogOnChoosingTestingMode(QDialog, Ui_choosing_dialog):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.setupUi(self)
        self.btn_get_test.clicked.connect(self.start_test)
        self.btn_add_test.clicked.conncet(self.add_test)

    '''
    def closeEvent(self, event):
        self.parent.already_test_exists = False
        super().closeEvent()
    '''
    
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

    def choose_task_type(self):
        open_warning_dialog(self, 'Выбирайте с умом',
                                "Учтите уже введщённые данные по заданию" +
                            " при выборе типа задания, пожалуйста!")
        i, okBtnPressed = QInputDialog.getItem(self,
                                               "Тип задания",
                                               "Выберите тип задания",
                                               REGIMS.keys(), 1, False)
        if okBtnPressed:
            self.mode = REGIMS[i]
        self.rewrite()
            
    def add_variant(self):
        if self.mode == 1:
            open_warning_dialog(self, 'Неверный тип задания',
                                "Выберите другой тип задания")
            return None
        if len(self.variants) == 4:
            open_warning_dialog(self, 'Слишком много вариантов',
                                "Введённый далее вариант перезапишет последний!")
        i, okBtnPressed = QInputDialog.getText(
            self, "Добавление варианта ответа", "Введите вариант ответа")
        if okBtnPressed:
            if len(self.variants) == 4:
                self.variants[-1] = i
            else:
                self.variants.append(i)
        self.rewrite()

    def add_right_variant_number(self):
        if self.mode == 1:
            open_warning_dialog(self, 'Неверный тип задания',
                                "Выберите другой тип задания")
            return None
        if self.mode == 2 and len(self.numbers) == 1:
            open_warning_dialog(self, 'Слишком много цифр',
                                "виду выбранного вами типа задания," +
                                " введённый далее номер варианта ответа" +
                                " перезапишет уже имеющийся")
        i, okBtnPressed = QInputDialog.getInt(
            self, "Правильный ответ", "Введите номер правильного ответа",
            1, 1, len(self.variants), 1)
        if okBtnPressed:
            if self.mode == 2:
                self.numbers = [i]
            else:
                self.numbers.append(i)
        self.rewrite()

    def rewrite(self):
        self.label_task_type.setText(REGIMS_BACKWARDS[self.mode])
        self.label_task_type.resize(self.label_task_type.sizeHint())
        self.plainTextEdit_2.setText('\n'.join(self.variants))
        self.label_right_variants_numbers.setText(self.numbers)
        self.label_right_variants_numbers.resize(self.label_right_variants_numbers.sizeHint())
        
    def submit(self):
        add_task(typ=self.mode, task_text=self.plainTextEdit.text(), variants=self.variants,
                 right_nums=self.numbers)
        open_warning_dialog(self, "Успешно!", "Вопрос добавлен в реестр!")

    def my_exit(self):
        super().closeEvent()


REGIMS = {"Ввод пользовательского ответа": 1,
          "Выбор одного из предложенных вариантов": 2,
          "Выбор нескольких из предложенных вариантов": 3}

REGIMS_BACKWARDS = {i[1]:i[0] for i in REGIMS.items()}


if __name__ == '__main__':
    app = QApplication(sys.argv)
