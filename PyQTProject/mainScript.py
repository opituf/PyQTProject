from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QPushButton, QDialog, QLineEdit, QMessageBox, QListView, QListWidget, QScrollArea, QTextEdit
from PyQt6.uic import loadUi
import sqlite3


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registerWindow.ui', self)
        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()

        self.password_form = self.findChild(QLineEdit, 'passwordForm')
        self.name_form = self.findChild(QLineEdit, 'nameForm')
        self.reg_btn = self.findChild(QPushButton, 'regBtn')
        self.enter_btn = self.findChild(QPushButton, 'enterBtn')

        self.reg_btn.clicked.connect(self.registration)
        self.enter_btn.clicked.connect(self.login)

    def registration(self):
        if self.name_form.text() and self.password_form.text():
            try:
                self.cursor.execute(
                    f"""INSERT INTO users (name, password, lessons) VALUES ({self.name_form.text()}, {self.password_form.text()}, 0)""")
                self.connection.commit()
                QMessageBox.information(self, "Успех", "Пользователь успешно создан")
                self.password_form.clear()
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Ошибка", "Имя пользователя уже существует.")
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните оба поля для регистрации.")

    def login(self):
        if self.name_form.text() and self.password_form.text():
            check = self.cursor.execute(
                f"""SELECT * FROM users WHERE name = {self.name_form.text()} and password = {self.password_form.text()}""").fetchall()
            if len(check) != 0:
                self.id = check[0][0]
                self.main_wind = MainWindow(self.id)
                self.main_wind.show()
            else:
                QMessageBox.warning(self, "Ошибка", "Имя или пароль неверны")
                self.password_form.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Имя или пароль неверны")
            self.password_form.clear()
            self.name_form.clear()


class MainWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)
        self.user_id = user_id  # Сохраняем только id пользователя

        self.stacked_wid = self.findChild(QStackedWidget, 'stackedWidget')
        self.page1_btn = self.findChild(QPushButton, 'page1_btn')
        self.page2_btn = self.findChild(QPushButton, 'page2_btn')
        self.page3_btn = self.findChild(QPushButton, 'page3_btn')

        self.page1_btn.clicked.connect(self.changePage)
        self.page2_btn.clicked.connect(self.changePage)
        self.page3_btn.clicked.connect(self.changePage)

        self.lesson_list = self.findChild(QListWidget, 'lessonList')
        self.lesson_list.itemDoubleClicked.connect(self.openLesson)
        self.showLessons()

    def getUserData(self):
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        user_data = cursor.execute("SELECT * FROM users WHERE id = ?", (self.user_id,)).fetchone()
        connection.close()
        return user_data

    def changePage(self):
        sender = self.sender()
        if sender == self.page1_btn:
            self.stacked_wid.setCurrentIndex(0)
        elif sender == self.page2_btn:
            self.stacked_wid.setCurrentIndex(1)
        else:
            self.stacked_wid.setCurrentIndex(2)

    def showLessons(self):
        connection = sqlite3.connect("lessons.db")
        cursor = connection.cursor()
        user_data = self.getUserData()  # Получаем данные пользователя
        lessons = user_data[3]  # Получаем строку с уроками
        if lessons:
            lesson_ids = lessons.split(', ')
        else:
            lesson_ids = [0]
        for i in lesson_ids:
            try:
                lesson = cursor.execute(f"""SELECT name FROM lessons WHERE id = {i}""").fetchone()
                if lesson:
                    self.lesson_list.addItem(lesson[0])
            except Exception as e:
                print(f"Ошибка при получении урока: {e}")

    def openLesson(self, item):
        label = item.text()

        # Получаем урок
        connectionLes = sqlite3.connect("lessons.db")
        connectionUser = sqlite3.connect("users.db")
        cursorLes = connectionLes.cursor()
        cursorUser = connectionUser.cursor()

        lesson = cursorLes.execute("SELECT text, id FROM lessons WHERE name = ?", (label,)).fetchall()
        lesson_text = lesson[0][0]
        lesson_id = lesson[0][1]

        # Получаем данные о текущих уроках пользователя
        user_data = self.getUserData()
        current_lessons = user_data[3]
        if current_lessons:
            lesson_ids = list(map(int, current_lessons.split(', ')))
        else:
            lesson_ids = [0]

        # Добавляем новый урок, если он не добавлен
        if lesson_id + 1 not in lesson_ids:
            new_lesson_id = lesson_id + 1
            lesson_ids.append(new_lesson_id)
            updated_lessons = ', '.join(map(str, lesson_ids))

            # Обновляем данные пользователя в базе данных
            cursorUser.execute(
                """UPDATE users SET lessons = ? WHERE id = ?""", (updated_lessons, self.user_id)
            )
            connectionUser.commit()

        # Открываем окно с текстом урока
        self.text_book = TextBook(label, lesson_text)
        self.text_book.show()

        self.lesson_list.clear()
        self.showLessons()


class TextBook(QWidget):
    def __init__(self, label, text):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle(f"Тема: {label}")

        # Создаем вертикальный layout для размещения виджетов
        layout = QVBoxLayout()

        # Создаем и настраиваем заголовок
        title_label = QLabel(f"<b>{label}</b>")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Создаем и настраиваем текстовый редактор
        self.text_edit = QTextEdit(self)
        text = text.replace(r"\n", "\n")  # Заменяем строковые символы \n на реальные переносы строк
        self.text_edit.setPlainText(text)
        self.text_edit.setReadOnly(True)  # Делаем редактор только для чтения
        self.text_edit.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)  # Включаем перенос слов

        # Добавляем виджеты в layout
        layout.addWidget(title_label)
        layout.addWidget(self.text_edit)

        # Устанавливаем layout для окна
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = RegisterWindow()
    window.show()
    app.exec()
