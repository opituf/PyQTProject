from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QPushButton, QDialog
from PyQt6.uic import loadUi
from lessons import Ui_lesson1, Ui_lesson2, Ui_lesson3, Ui_lesson4, Ui_lesson5


class Lesson1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/lesson1.ui', self)


class Lesson2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/lesson2.ui', self)


class Lesson3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/lesson3.ui', self)


class Lesson4(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/lesson4.ui', self)


class Lesson5(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/lesson5.ui', self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)

        self.stacked_wid = self.findChild(QStackedWidget, 'stackedWidget')
        self.page1_btn = self.findChild(QPushButton, 'page1_btn')
        self.page2_btn = self.findChild(QPushButton, 'page2_btn')

        self.page1_btn.clicked.connect(self.changePage)
        self.page2_btn.clicked.connect(self.changePage)

        self.btn_lesson1 = self.findChild(QPushButton, 'lesson1_btn')
        self.btn_lesson2 = self.findChild(QPushButton, 'lesson2_btn')
        self.btn_lesson3 = self.findChild(QPushButton, 'lesson3_btn')
        self.btn_lesson4 = self.findChild(QPushButton, 'lesson4_btn')
        self.btn_lesson5 = self.findChild(QPushButton, 'lesson5_btn')

        self.btn_lesson1.clicked.connect(self.open_lesson)
        self.btn_lesson2.clicked.connect(self.open_lesson)
        self.btn_lesson3.clicked.connect(self.open_lesson)
        self.btn_lesson4.clicked.connect(self.open_lesson)
        self.btn_lesson5.clicked.connect(self.open_lesson)

    def changePage(self):
        sender = self.sender()
        if sender == self.page1_btn:
            self.stacked_wid.setCurrentIndex(0)
        else:
            self.stacked_wid.setCurrentIndex(1)

    def open_lesson(self):
        sender = self.sender()
        self.new_window = Lesson1()
        if sender == self.btn_lesson1:
            self.new_window.show()
        elif sender == self.btn_lesson2:
            self.new_window = Lesson2()
            self.new_window.show()
        elif sender == self.btn_lesson3:
            self.new_window = Lesson3()
            self.new_window.show()
        elif sender == self.btn_lesson4:
            self.new_window = Lesson4()
            self.new_window.show()
        elif sender == self.btn_lesson5:
            self.new_window = Lesson5()
            self.new_window.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
