from user import User
from admin import Admin
from manager import Manager
from customer import Customer


def first_menu_controller(put):
    if put == 1:
        role = user.login_to_account()
        if role == "admin":
            admin_menu()
        elif role == "manager":
            manager_menu()
        elif role == "customer":
            customer_menu()
    elif put == 2:
        user.registration_user()


def admin_menu_controller(put):
    if put == 1:
        admin.display_all_users()
    elif put == 2:
        admin.display_all_users()
        user_id = int(input("Введите id клиента: "))
        new_role = input("Введите новую роль для клиента: ")
        admin.change_user_role(user_id, new_role)
    elif put == 3:
        admin.display_all_users()
        user_id = int(input("Введите id клиента: "))
        admin.dell_user(user_id)

def customer_menu_controller(put):
    if put == 1:
        customer.display_all_products()
    elif put == 2:
        customer.display_sort_min()

def manager_menu_controller(put):
    if put == 1:
        manager.create_products_table()
        manager.import_products()
    elif put == 2:
        manager.display_all_products()
    elif put == 3:
        manager.add_product()
    elif put == 4:
        manager.dell_product()

def admin_menu():
    while True:
        print("""
        #############################################
        ##      Приветствую Вас!!!                 ##
        ##                                         ## 
        ##  1. Просмотреть всех пользователей.     ##
        ##  2. Изменить роль пользователей.        ##
        ##  3. Удалить пользователя.               ##
        ##  4. Выйти.                              ##
        ##                                         ##
        #############################################
        """)

        try:
            put = int(input("Выберите нужный пункт меню: "))
            if put == 4:
                break
        except ValueError:
            print("Вы ввели не корректное значение.")
        else:
            if put in [1, 2, 3]:
                admin_menu_controller(put)

def manager_menu():
    while True:
        print("""
            ################################################
            ##      Приветствую Вас!!!                    ##
            ##                                            ## 
            ##  1. Импортировать таблицу с csv файла.     ##
            ##  2. Вывести таблицу продуктов.             ##
            ##  3. Добавить товар.                        ##
            ##  4. Удалить товар.                         ##
            ##  5. Выйти.                                 ##
            ##                                            ##
            ################################################
            """)

        try:
            put = int(input("Выберите нужный пункт меню: "))
            if put == 5:
                break
        except ValueError:
            print("Вы ввели не корректное значение.")
        else:
            if put in [1, 2, 3, 4]:
                manager_menu_controller(put)

def customer_menu():
    while True:
        print("""
            ################################################
            ##      Приветствую Вас!!!                    ##
            ##                                            ## 
            ##  1. Вывести таблицу продуктов.             ##
            ##  2. Сортировать таблицу продуктов по цене. ##
            ##  3. Выйти.                                 ##
            ##                                            ##
            ################################################
            """)
        
        try:
            put = int(input("Выберите нужный пункт меню: "))
            if put == 3:
                break
        except ValueError:
            print("Вы ввели не корректное значение.")
        else:
            if put in [1, 2]:
                customer_menu_controller(put)


def main():
    while True:
        print("""
        #####################################
        ##      Приветствую Вас!!!         ##
        ##                                 ## 
        ##  1. Войти в личный кабинет.     ##
        ##  2. Зарегестрироваться.         ##
        ##  3. Выйти.                      ##
        ##                                 ##
        #####################################
        """)

        try:
            put = int(input("Выберите нужный пункт меню: "))
            if put == 3:
                print("До скорой встречи!!!")
                break
        except ValueError:
            print("Вы ввели не корректное значение.")
        else:
            if put in [1, 2]:
                first_menu_controller(put)


if __name__ == "__main__":
    print("main.py запущена сама по себе.")
    user = User()
    admin = Admin()
    manager = Manager()
    customer = Customer()
    try:
        main()
    finally:
        user.close_connection_user()
        manager.close_connection_manager()
else:
    print("main.py импортированна.")
