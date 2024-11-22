from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QPushButton
from lessons import Ui_lesson1, Ui_lesson2, Ui_lesson3, Ui_lesson4, Ui_lesson5


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)

        self.stacked_wid = self.findChild(QStackedWidget, 'stackedWidget')
        self.page1_btn = self.findChild(QPushButton, 'page1_btn')
        self.page2_btn = self.findChild(QPushButton, 'page2_btn')

        self.page1_btn.clicked.connect(self.show_textbook)
        self.page2_btn.clicked.connect(self.show_prefabs)

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

    def show_textbook(self):
        self.stacked_wid.setCurrentIndex(0)

    def show_prefabs(self):
        self.stacked_wid.setCurrentIndex(1)

    def open_lesson(self):
        sender = self.sender()
        new_ui_widget = QWidget()
        ui = Ui_lesson1()


        if sender == self.btn_lesson1:
            ui = Ui_lesson1()
        elif sender == self.btn_lesson2:
            ui = Ui_lesson2()
        elif sender == self.btn_lesson3:
            ui = Ui_lesson3()
        elif sender == self.btn_lesson4:
            ui = Ui_lesson4()
        elif sender == self.btn_lesson5:
            ui = Ui_lesson5()

        ui.setupUi(new_ui_widget)
        new_ui_widget.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
