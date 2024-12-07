from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QPushButton, QDialog, QLineEdit, QMessageBox, QListView, QListWidget, QScrollArea, QTextEdit, QHBoxLayout, \
    QInputDialog, QFileDialog
from PyQt6.uic import loadUi
import sqlite3
from PyQt6.QtGui import QClipboard


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registerWindow.ui', self)  # Загружаем UI из файла
        self.connection = sqlite3.connect("users.db")  # Подключаемся к базе данных пользователей
        self.cursor = self.connection.cursor()  # Создаем курсор для выполнения запросов

        # Получаем доступ к элементам интерфейса
        self.password_form = self.findChild(QLineEdit, 'passwordForm')
        self.name_form = self.findChild(QLineEdit, 'nameForm')
        self.reg_btn = self.findChild(QPushButton, 'regBtn')
        self.enter_btn = self.findChild(QPushButton, 'enterBtn')

        # Подключаем обработчики событий для кнопок
        self.reg_btn.clicked.connect(self.registration)
        self.enter_btn.clicked.connect(self.login)

    def registration(self):
        # Проверяем, что оба поля заполнены
        if self.name_form.text() and self.password_form.text():
            try:
                # Выполняем запрос на добавление нового пользователя в базу данных
                self.cursor.execute(
                    f"""INSERT INTO users (name, password, lessons) VALUES ({self.name_form.text()}, {self.password_form.text()}, 0)""")
                self.connection.commit()  # Сохраняем изменения в базе данных
                QMessageBox.information(self, "Успех", "Пользователь успешно создан")  # Показываем сообщение
                self.password_form.clear()  # Очищаем поле пароля
            except sqlite3.IntegrityError:
                # Если имя пользователя уже существует, выводим предупреждение
                QMessageBox.warning(self, "Ошибка", "Имя пользователя уже существует.")
        else:
            # Если поля не заполнены, выводим предупреждение
            QMessageBox.warning(self, "Ошибка", "Заполните оба поля для регистрации.")

    def login(self):
        # Проверяем, что оба поля заполнены
        if self.name_form.text() and self.password_form.text():
            # Выполняем запрос для проверки введенных данных
            check = self.cursor.execute(
                f"""SELECT * FROM users WHERE name = {self.name_form.text()} and password = {self.password_form.text()}""").fetchall()
            if len(check) != 0:
                self.id = check[0][0]  # Сохраняем ID пользователя
                self.main_wind = MainWindow(self.id)  # Создаем главное окно
                self.main_wind.show()  # Показываем главное окно
            else:
                # Если данные неверные, выводим предупреждение
                QMessageBox.warning(self, "Ошибка", "Имя или пароль неверны")
                self.password_form.clear()  # Очищаем поле пароля
        else:
            # Если поля не заполнены, выводим предупреждение
            QMessageBox.warning(self, "Ошибка", "Имя или пароль неверны")
            self.password_form.clear()  # Очищаем поле пароля
            self.name_form.clear()  # Очищаем поле имени


class MainWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)  # Загружаем UI главного окна
        self.user_id = user_id  # Сохраняем ID пользователя

        # Получаем доступ к элементам интерфейса
        self.stacked_wid = self.findChild(QStackedWidget, 'stackedWidget')
        self.page1_btn = self.findChild(QPushButton, 'page1_btn')
        self.page2_btn = self.findChild(QPushButton, 'page2_btn')
        self.page3_btn = self.findChild(QPushButton, 'page3_btn')

        # Подключаем обработчики событий для кнопок
        self.page1_btn.clicked.connect(self.changePage)
        self.page2_btn.clicked.connect(self.changePage)
        self.page3_btn.clicked.connect(self.changePage)

        # Получаем доступ к спискам
        self.lesson_list = self.findChild(QListWidget, 'lessonList')
        self.lesson_list.itemDoubleClicked.connect(self.openLesson)
        self.showLessons()  # Показываем уроки

        self.prefabs_list = self.findChild(QListWidget, 'prefabsList')
        self.prefabs_list.itemDoubleClicked.connect(self.openPrefab)
        self.showPrefabs()  # Показываем префабы

        self.submit_prefab_btn = self.findChild(QPushButton, 'submitPrefab')
        self.prefab_text = self.findChild(QLineEdit, 'prefabText')
        self.submit_prefab_btn.clicked.connect(self.addPrefab)


    def getUserData(self):
        # Функция для получения данных пользователя из базы данных
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        user_data = cursor.execute("SELECT * FROM users WHERE id = ?", (self.user_id,)).fetchone()
        connection.close()  # Закрываем соединение с базой данных
        return user_data

    def changePage(self):
        # Функция для изменения страницы в stackedWidget
        sender = self.sender()  # Получаем источник сигнала
        if sender == self.page1_btn:
            self.stacked_wid.setCurrentIndex(0)  # Переключаем на первую страницу
        elif sender == self.page2_btn:
            self.stacked_wid.setCurrentIndex(1)  # Переключаем на вторую страницу
        else:
            self.stacked_wid.setCurrentIndex(2)  # Переключаем на третью страницу

    def showLessons(self):
        # Функция для отображения списка уроков
        connection = sqlite3.connect("lessons.db")
        cursor = connection.cursor()
        user_data = self.getUserData()  # Получаем данные пользователя
        lessons = user_data[3]  # Получаем строку с уроками
        if lessons:
            lesson_ids = lessons.split(', ')  # Разбиваем строку на ID уроков
        else:
            lesson_ids = [0]  # Если уроков нет, используем пустой список
        for i in lesson_ids:
            try:
                # Выполняем запрос для получения информации о каждом уроке
                lesson = cursor.execute(f"""SELECT name FROM lessons WHERE id = {i}""").fetchone()
                if lesson:
                    self.lesson_list.addItem(lesson[0])  # Добавляем урок в список
            except Exception as e:
                print(f"Ошибка при получении урока: {e}")

    def openLesson(self, item):
        # Функция для открытия урока
        label = item.text()  # Получаем текст (название) выбранного урока

        # Получаем данные о выбранном уроке
        connectionLes = sqlite3.connect("lessons.db")
        connectionUser = sqlite3.connect("users.db")
        cursorLes = connectionLes.cursor()
        cursorUser = connectionUser.cursor()

        lesson = cursorLes.execute("SELECT text, id FROM lessons WHERE name = ?", (label,)).fetchall()
        lesson_text = lesson[0][0]  # Текст урока
        lesson_id = lesson[0][1]  # ID урока

        # Получаем текущие данные о уроках пользователя
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
            connectionUser.commit()  # Сохраняем изменения в базе данных

        # Открываем окно с текстом урока
        self.text_book = TextBook(label, lesson_text)
        self.text_book.show()

        # Обновляем список уроков
        self.lesson_list.clear()
        self.showLessons()

    def showPrefabs(self):
        # Функция для отображения списка префабов
        connection = sqlite3.connect("prefabs.db")
        cursor = connection.cursor()

        # Используем параметризованный запрос
        prefabs = cursor.execute("SELECT request FROM prefabs WHERE creator = ?", (self.user_id,)).fetchall()

        self.prefabs_list.clear()  # Очищаем текущий список

        # Добавляем каждый элемент из полученных данных
        for prefab in prefabs:
            if prefab and prefab[0]:  # Проверка на пустоту или None
                self.prefabs_list.addItem(str(prefab[0]))  # Преобразуем число в строку перед добавлением

        connection.close()  # Закрытие соединения

    def openPrefab(self, item):
        text = item.text()
        self.opened_prefab = CopyBook(text, self)  # Передаем текущий объект MainWindow в CopyBook
        self.opened_prefab.show()

    def addPrefab(self):
        connection = sqlite3.connect("prefabs.db")
        cursor = connection.cursor()

        # Проверяем, что текст в поле для префаба не пустой
        if self.prefab_text.text().strip():  # .strip() удаляет пробелы по бокам
            try:
                # Параметризованный запрос для добавления префаба
                cursor.execute("INSERT INTO prefabs (creator, request) VALUES (?, ?)",
                               (self.user_id, self.prefab_text.text()))
                connection.commit()  # Подтверждаем изменения
                self.prefab_text.clear()  # Очищаем поле для ввода
                self.stacked_wid.setCurrentIndex(1)
                self.showPrefabs()  # Обновляем список префабов
            except sqlite3.Error as e:
                # Обработка ошибки при выполнении запроса
                QMessageBox.warning(self, "Ошибка", f"Произошла ошибка при добавлении префаба: {e}")
        else:
            QMessageBox.warning(self, "Ошибка", "Поле префаба не может быть пустым.")

        connection.close()  # Закрываем соединение с базой данных


class TextBook(QWidget):
    def __init__(self, label, text):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle(f"Тема: {label}")

        # Создаем вертикальный layout для размещения виджетов
        layout = QVBoxLayout()

        # Создаем и настраиваем заголовок
        title_label = QLabel(f"<b>{label}</b>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Создаем и настраиваем текстовый редактор
        self.text_edit = QTextEdit(self)
        text = text.replace(r"\n", "\n")  # Заменяем строковые символы \n на реальные переносы строк
        self.text_edit.setPlainText(text)  # Устанавливаем текст в редактор
        self.text_edit.setReadOnly(True)  # Делаем редактор только для чтения
        self.text_edit.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)  # Включаем перенос слов

        # Создаем кнопку для сохранения
        save_button = QPushButton("Сохранить текст", self)
        save_button.clicked.connect(self.save_text)  # Подключаем слот для сохранения текста

        # Добавляем виджеты в layout
        layout.addWidget(title_label)
        layout.addWidget(self.text_edit)
        layout.addWidget(save_button)  # Добавляем кнопку в layout

        # Устанавливаем layout для окна
        self.setLayout(layout)

    def save_text(self):
        # Открываем диалог выбора места для сохранения файла
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить текст", "", "Text Files (*.txt);;All Files (*)")

        if file_name:
            # Получаем текст из редактора
            text_to_save = self.text_edit.toPlainText()

            try:
                # Открываем файл на запись
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(text_to_save)
                print(f"Текст успешно сохранен в {file_name}")
            except Exception as e:
                print(f"Ошибка при сохранении файла: {e}")

class CopyBook(QWidget):
    def __init__(self, text, main_window):
        super().__init__()
        self.text = text
        self.main_window = main_window  # Сохраняем ссылку на MainWindow

        # Заголовок для SQL запроса
        self.query_label = QLabel(text)
        self.query_label.setStyleSheet("font-size: 15px; font-weight: bold;")

        # Кнопки для действий
        self.copy_button = QPushButton("Копировать")
        self.copy_button.clicked.connect(self.copy_query)

        self.edit_button = QPushButton("Изменить")
        self.edit_button.clicked.connect(self.edit_query)

        self.delete_button = QPushButton("Удалить")
        self.delete_button.clicked.connect(self.delete_query)

        # Вертикальное размещение элементов
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)

        layout = QVBoxLayout()
        layout.addWidget(self.query_label)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setWindowTitle("Запрос")
        self.setGeometry(100, 100, 400, 100)

    def copy_query(self):
        query = self.query_label.text()

        # Получаем доступ к буферу обмена через приложение
        clipboard = QApplication.clipboard()

        # Копируем текст в буфер обмена
        clipboard.setText(query)

    def edit_query(self):
        connection = sqlite3.connect("prefabs.db")
        cursor = connection.cursor()
        # Здесь будет логика для редактирования запроса
        new_query, ok = QInputDialog.getText(self, "Редактировать запрос", "Введите новый SQL запрос:",
                                             text=self.query_label.text())
        if ok:
            self.query_label.setText(new_query)
            # Параметризированный запрос, чтобы избежать SQL инъекций
            cursor.execute("UPDATE prefabs SET request = ? WHERE request = ?", (new_query, self.text))
            connection.commit()  # Подтверждаем изменения в базе данных
        connection.close()
        self.main_window.showPrefabs()

    def delete_query(self):
        # Запрос для удаления префаба из базы данных
        connection = sqlite3.connect("prefabs.db")
        cursor = connection.cursor()

        # Выполняем запрос на удаление префаба
        cursor.execute("DELETE FROM prefabs WHERE request = ?", (self.text,))
        connection.commit()  # Сохраняем изменения в базе данных
        connection.close()

        # Очищаем текстовое поле
        self.query_label.clear()
        print("Запрос удален")

        # Обновляем список префабов в MainWindow
        self.main_window.showPrefabs()


if __name__ == "__main__":
    app = QApplication([])  # Создаем приложение
    window = RegisterWindow()  # Создаем окно регистрации
    window.show()  # Показываем окно
    app.exec()  # Запускаем главный цикл приложения
