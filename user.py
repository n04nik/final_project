import sqlite3
import re
import pwinput


class User:
    """Класс User необходим для создание базы users и работы с этой базой."""
    def __init__(self):
        """Конструктор класса User"""
        self.connect = sqlite3.connect("users.sqlite3")
        self.c = self.connect.cursor()
        self.create_users_table()

    def create_users_table(self):
        """Создание базы users"""
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT NOT NULL,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telephone TEXT NOT NULL,
                    role TEXT NULL
                    );""")

    def login_to_account(self):
        """Вход в личный кабинет по логину и поролю, функция возвращает роль для дальнейшего вывода нужного меню."""
        while True:
            login = input("Введите свой login: ")       
            password = pwinput.pwinput('Введите пароль: ', '*')
        
            self.c.execute("SELECT role FROM users WHERE login = ? AND password = ?;", (login, password))
            result = self.c.fetchone()

            if result:
                role = result[0]
                print(f"Добро пожаловать, {login}")
                print(role)
                return role        
            else:
                print("Не верный login или password!")
            break

    def registration_user(self):
        """Регистрация пользователя с проверкой на наличие уже зарегестрированных пользователей по email и номеру телефона."""
        while True:
            login = input("Введите свой login: ")
            if len(login) == 0 or login.isspace():
                raise NameExc("Недопустимое значение login.")

            if login.lower() == "admin":
                print("Это имя login зарезервировано!")
                continue
            else:
                break
        res_login = self.find_login(login)
        if res_login:
            raise NameExc("Этот login уже зарегестрирован")

        user_name = input("Введите свою имя: ")
        if len(user_name) == 0 or user_name.isspace():
            raise NameExc("Недопустимое значение имени.")

        user_surname = input("Введите свою фамилию: ")
        if len(user_surname) == 0 or user_surname.isspace():
            raise NameExc("Недопустимое значение фамилии.")

        password = pwinput.pwinput('Введите пароль: ', '*')  # Используем метод pwinput для маскирования пароля при вводе.
        if len(password) == 0 or password.isspace():
            raise NameExc("Недопустимое значение пароля.")

        while True:
            email = input("Введите свой email: ")
            if len(email) == 0 or email.isspace():
                raise NameExc("Недопустимое значение email!")
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):  # Через регулярное выражение проверяем формат введенного email.
                print("Неверный формат email.")
                continue
            else:
                break

        res_email = self.find_email(email)
        if res_email:
            raise NameExc("Этот email уже зарегестрирован!")

        while True:
            telephone = input("Введите свой номер телефона в формате '+375 (29/25/33) 1111111': ") 
            if len(telephone) == 0 or telephone.isspace():
                raise NameExc("Недопустимое значение номера телефона")
            if not re.match(r'^\+375 \(\d{2}\) \d{7}$', telephone):  # Через регулярное выражение проверяем формат введенного номера телефона.
                print("Неверный формат номера телефона.")
                continue
            else:
                break

        res_telephone = self.find_telephone(telephone)
        if res_telephone:
            raise NameExc("Этот номер телефона уже зарегестрирован")

        self.c.execute("INSERT INTO users (login, name, surname, password, email, telephone, role) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (login, user_name, user_surname, password, email, telephone, "None"))
        self.connect.commit()

    def find_login(self, login):

        self.c.execute("SELECT id FROM users WHERE login = ?;", (login,))
        return self.c.fetchone()

    def find_email(self, email):

        self.c.execute("SELECT id FROM users WHERE email = ?;", (email,))
        return self.c.fetchone()

    def find_telephone(self, telephone):

        self.c.execute("SELECT id FROM users WHERE telephone = ?;", (telephone,))
        return self.c.fetchone()

    def close_connection_user(self):
        print("До скорой встречи!!!")
        self.connect.close()


class NameExc(Exception):
    """Класс для обработки ошибок"""
    def __init__(self, message="Недопустимое значение."):
        self.message = message
        super().__init__(self.message)
        

class EmailExc(NameExc):
    def __init__(self, message="Недопустимое значение email"):
        super().__init__(message)


class TelephoneExc(NameExc):
    def __init__(self, message="Недопустимое значение номера телефона."):
        super().__init__(message)
    