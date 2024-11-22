from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lesson1(object):
    def setupUi(self, lesson1):
        lesson1.setObjectName("lesson1")
        lesson1.resize(750, 470)
        self.centralwidget = QtWidgets.QWidget(parent=lesson1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 750, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        lesson1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=lesson1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        lesson1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=lesson1)
        self.statusbar.setObjectName("statusbar")
        lesson1.setStatusBar(self.statusbar)

        self.retranslateUi(lesson1)
        QtCore.QMetaObject.connectSlotsByName(lesson1)

    def retranslateUi(self, lesson1):
        _translate = QtCore.QCoreApplication.translate
        lesson1.setWindowTitle(_translate("lesson1", "MainWindow"))
        self.label.setText(_translate("lesson1", "Урок 1: Основы SQL — Выборка данных\n"
"Цель урока: Научиться извлекать данные из таблиц с помощью запроса SELECT.\n"
"\n"
"Что такое запрос SELECT?\n"
"Запрос SELECT используется для извлечения данных из одной или нескольких колонок таблицы.\n"
"\n"
"Простой запрос для выборки всех данных:\n"
"SELECT column1, column2, ... FROM table_name;\n"
"Для выбора всех данных из таблицы можно использовать *, что означает «все колонки».\n"
"\n"
"Примеры запросов\n"
"Выбор всех колонок:\n"
"SELECT * FROM employees;\n"
"Этот запрос выберет все строки и все колонки из таблицы employees.\n"
"\n"
"Выбор определённых колонок: Если нужно выбрать только некоторые данные, указывайте имена колонок через запятую:\n"
"SELECT name, age FROM employees;\n"
"Этот запрос вернёт только имена и возраст сотрудников.\n"
"\n"
"Выбор данных с псевдонимами (алиасами): Для удобства можно использовать псевдонимы для отображения колонок:\n"
"SELECT name AS \"Employee Name\", age AS \"Employee Age\" FROM employees;\n"
"Этот запрос отобразит столбцы с именами \"Employee Name\" и \"Employee Age\" вместо стандартных названий колонок.\n"
"\n"
"Важные моменты:\n"
"* используется для выбора всех колонок таблицы.\n"
"Псевдонимы (aliase) упрощают чтение результатов запроса."))


class Ui_lesson2(object):
    def setupUi(self, lesson2):
        lesson2.setObjectName("lesson2")
        lesson2.resize(1030, 500)
        self.centralwidget = QtWidgets.QWidget(parent=lesson2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1030, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        lesson2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=lesson2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 21))
        self.menubar.setObjectName("menubar")
        lesson2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=lesson2)
        self.statusbar.setObjectName("statusbar")
        lesson2.setStatusBar(self.statusbar)

        self.retranslateUi(lesson2)
        QtCore.QMetaObject.connectSlotsByName(lesson2)

    def retranslateUi(self, lesson2):
        _translate = QtCore.QCoreApplication.translate
        lesson2.setWindowTitle(_translate("lesson2", "MainWindow"))
        self.label.setText(_translate("lesson2", "Урок 2: Фильтрация данных с помощью оператора WHERE\n"
"Цель урока: Научиться фильтровать строки с помощью оператора WHERE.\n"
"\n"
"Основной синтаксис запроса:\n"
"SELECT column1, column2 FROM table_name WHERE condition;\n"
"Оператор WHERE позволяет фильтровать данные, чтобы выбрать только те строки, которые соответствуют указанному условию.\n"
"\n"
"Примеры использования оператора WHERE\n"
"Пример 1: Простая фильтрация\n"
"Выбор сотрудников с должностью \"Менеджер\":\n"
"SELECT name, position FROM employees WHERE position = \'Менеджер\';\n"
"\n"
"Пример 2: Фильтрация с несколькими условиями (AND и OR)\n"
"Можно использовать операторы AND и OR, чтобы указать несколько условий.\n"
"\n"
"Пример с AND: выберем сотрудников старше 30 лет с должностью \"Менеджер\":\n"
"SELECT name, age, position FROM employees WHERE age > 30 AND position = \'Менеджер\';\n"
"\n"
"Пример с OR: выберем сотрудников с должностями \"Менеджер\" или \"Директор\":\n"
"SELECT name, position FROM employees WHERE position = \'Менеджер\' OR position = \'Директор\';\n"
"\n"
"Пример 3: Использование оператора IN\n"
"Если нужно проверить несколько возможных значений, используйте IN. Например, выбираем сотрудников с должностями \"Менеджер\" или \"Директор\":\n"
"SELECT name, position FROM employees WHERE position IN (\'Менеджер\', \'Директор\');\n"
"\n"
"Пример 4: Использование BETWEEN для диапазонов\n"
"Когда нужно выбрать значения, попадающие в определённый диапазон, используйте BETWEEN. Например, выбираем сотрудников в возрасте от 25 до 40 лет:\n"
"SELECT name, age FROM employees WHERE age BETWEEN 25 AND 40;"))


class Ui_lesson3(object):
    def setupUi(self, lesson3):
        lesson3.setObjectName("lesson3")
        lesson3.resize(700, 400)
        self.centralwidget = QtWidgets.QWidget(parent=lesson3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 670, 350))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        lesson3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=lesson3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        lesson3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=lesson3)
        self.statusbar.setObjectName("statusbar")
        lesson3.setStatusBar(self.statusbar)

        self.retranslateUi(lesson3)
        QtCore.QMetaObject.connectSlotsByName(lesson3)

    def retranslateUi(self, lesson3):
        _translate = QtCore.QCoreApplication.translate
        lesson3.setWindowTitle(_translate("lesson3", "MainWindow"))
        self.label.setText(_translate("lesson3", "Урок 3: Сортировка данных с помощью оператора ORDER BY\n"
"Цель урока: Научиться сортировать данные по возрастанию или убыванию с помощью оператора ORDER BY.\n"
"\n"
"Основной синтаксис запроса:\n"
"SELECT column1, column2 FROM table_name ORDER BY column1 ASC|DESC;\n"
"Оператор ORDER BY позволяет отсортировать данные по одному или нескольким столбцам. \n"
"По умолчанию сортировка идет по возрастанию (ASC), но можно указать сортировку по убыванию (DESC).\n"
"\n"
"Примеры использования оператора ORDER BY\n"
"\n"
"Пример 1: Сортировка по возрастанию\n"
"Сортируем сотрудников по возрасту от младшего к старшему:\n"
"SELECT name, age FROM employees ORDER BY age ASC;\n"
"\n"
"Пример 2: Сортировка по убыванию\n"
"Сортируем сотрудников по возрасту от старшего к младшему:\n"
"SELECT name, age FROM employees ORDER BY age DESC;\n"
"\n"
"Пример 3: Сортировка по нескольким столбцам\n"
"Сортировка сначала по возрасту (по возрастанию), затем по имени (по убыванию):\n"
"SELECT name, age FROM employees ORDER BY age ASC, name DESC;"))


class Ui_lesson4(object):
    def setupUi(self, lesson4):
        lesson4.setObjectName("lesson4")
        lesson4.resize(620, 530)
        self.centralwidget = QtWidgets.QWidget(parent=lesson4)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 600, 470))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        lesson4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=lesson4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        lesson4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=lesson4)
        self.statusbar.setObjectName("statusbar")
        lesson4.setStatusBar(self.statusbar)

        self.retranslateUi(lesson4)
        QtCore.QMetaObject.connectSlotsByName(lesson4)

    def retranslateUi(self, lesson4):
        _translate = QtCore.QCoreApplication.translate
        lesson4.setWindowTitle(_translate("lesson4", "MainWindow"))
        self.label.setText(_translate("lesson4", "Урок 4: Агрегатные функции — COUNT, AVG, SUM, MAX, MIN\n"
"Цель урока: Научиться использовать агрегатные функции для получения статистических данных.\n"
"\n"
"Агрегатные функции применяются к набору строк и возвращают одно значение для этого набора. \n"
"\n"
"К основным агрегатным функциям относятся:\n"
"COUNT — подсчет строк.\n"
"AVG — вычисление среднего значения.\n"
"SUM — вычисление суммы.\n"
"MAX — нахождение максимума.\n"
"MIN — нахождение минимума.\n"
"\n"
"Примеры использования агрегатных функций\n"
"\n"
"Пример 1: Подсчет количества строк\n"
"Подсчитываем общее количество записей в таблице employees:\n"
"SELECT COUNT(*) FROM employees;\n"
"\n"
"Пример 2: Среднее значение\n"
"Вычисляем средний возраст сотрудников:\n"
"SELECT AVG(age) FROM employees;\n"
"\n"
"Пример 3: Сумма значений\n"
"Вычисляем общую сумму зарплат сотрудников (предполагается наличие колонки salary):\n"
"SELECT SUM(salary) FROM employees;\n"
"\n"
"Пример 4: Максимальное и минимальное значение\n"
"Находим максимальный и минимальный возраст сотрудников:\n"
"SELECT MAX(age), MIN(age) FROM employees;"))


class Ui_lesson5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 790, 550))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Урок 5: Соединение таблиц с помощью оператора JOIN\n"
"Цель урока: Научиться объединять данные из нескольких таблиц с помощью операторов соединения JOIN.\n"
"\n"
"Оператор JOIN используется для объединения строк из двух и более таблиц на основе логического условия.\n"
"\n"
"Примеры использования оператора JOIN\n"
"Пример 1: Простое соединение JOIN\n"
"Для объединения данных из двух таблиц employees и departments,\n"
"где каждый сотрудник имеет ссылку на отдел через поле department_id:\n"
"SELECT employees.name, departments.name\n"
"FROM employees\n"
"JOIN departments ON employees.department_id = departments.id;\n"
"Этот запрос выберет имена сотрудников и названия их отделов.\n"
"\n"
"Пример 2: Соединение с фильтрацией\n"
"Можно добавить условие фильтрации после соединения. Например,\n"
"чтобы выбрать только тех сотрудников, которые работают в отделе \"HR\":\n"
"SELECT employees.name, departments.name\n"
"FROM employees\n"
"JOIN departments ON employees.department_id = departments.id\n"
"WHERE departments.name = \'HR\';\n"
"\n"
"Пример 3: Разные типы соединений\n"
"LEFT JOIN: Все строки из левой таблицы и совпадающие строки из правой.\n"
"RIGHT JOIN: Все строки из правой таблицы и совпадающие строки из левой.\n"
"FULL JOIN: Все строки из обеих таблиц.\n"
"\n"
"Пример с использованием LEFT JOIN:\n"
"SELECT employees.name, departments.name\n"
"FROM employees\n"
"LEFT JOIN departments ON employees.department_id = departments.id;\n"
"Этот запрос вернет все имена сотрудников и название их отдела, если они принадлежат какому-либо отделу.\n"
"Если сотрудник не относится ни к одному отделу, то для него будет выведено значение NULL в колонке с названием отдела.\n"
"\n"
""))
