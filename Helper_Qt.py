import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from main_window_ui import Ui_MainWindow
from dialog_to_choose_mode_in_testing_ui import Ui_Dialog as Ui_choosing_dialog

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.go_to_testing)
        self.already_test_exists = False

    def go_to_testing(self):
        if not self.already_test_exists:
            test_mode_choosing_dialog = DialogOnChoosingTestingMode(self)
            test_mode_choosing_dialog.show()
            self.already_test_exists = True

class DialogOnChoosingTestingMode(QDialog, Ui_choosing_dialog):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        self.setupUi(self)
        self.btn_get_test.clicked.connect(self.start_test)
        self.btn_add_test.clicked.conncet(self.add_test)

    def closeEvent(self, event):
        self.parent.already_test_exists = False
        super().closeEvent()

    def start_test(self):
        pass

    def add_test(self):
        pass
