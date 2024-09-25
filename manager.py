from user import User
import sqlite3
import csv


class Manager(User):
    def __init__(self):
        self.connect = sqlite3.connect("products.sqlite3")
        self.c = self.connect.cursor()
        self.create_products_table()

    def create_products_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    category TEXT NOT NULL,
                    manufacturer TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    quantity INT NOT NULL,
                    price REAL NOT NULL,
                    currency TEXT NOT NULL 
                    );""")
        
    def import_products(self):        
        with open("products.csv", "r", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.c.execute('''INSERT INTO products (product_id, category, manufacturer, product_name, quantity, price, currency)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (row['product_id'], row['category'], row['manufacturer'], row['product_name'], row['quantity'], row['price'], row['currency']))
        self.connect.commit()
        
    def close_connection_manager(self):
        self.connect.close()    
    
    def display_all_products(self):
        self.c.execute("SELECT product_id, category, manufacturer, product_name, quantity, price, currency FROM products;")
        products = self.c.fetchall()
        for product in products:
            print(product)        
    
    def add_product(self):
        while True:
            print("""
                  ##############################
                  ##    Выберите категорию:   ##
                  ##                          ##
                  ##  1. Видеокарта.          ##
                  ##  2. Процессор.           ##
                  ##  3. Материнская плата.   ##
                  ##  4. Оперативная память.  ##
                  ##  5. Выход.               ##
                  ##                          ##
                  ##############################
                  """)
            
            try:
                put = int(input("Выберите нужную категорию: "))    
                if put == 5:
                    break
            except ValueError:
                print("Вы ввели не корректное значение!")
            else:
                if put == 1: 
                    category = "Видеокарта"
                    break
                elif put == 2: 
                    category = "Процессор"
                    break
                elif put == 3: 
                    category = "Материнская плата"
                    break
                elif put == 4:
                    category = "Оперативная память"
                    break

        manufacturer = input("Введите производителя: ")
        if len(manufacturer) == 0 or manufacturer.isspace():
            raise ManufacturerExc("Недопустимое значение имени.")

        product_name = input("Введите название: ")
        if len(product_name) == 0 or product_name.isspace():
            raise ProductNameExc("Недопустимое значение фамилии.")

        quantity = int(input("Введите количество товара: "))

        price = float(input("Введите цену за единицу товара: "))

        self.c.execute("INSERT INTO products (category, manufacturer, product_name, quantity, price, currency) VALUES (?, ?, ?, ?, ?, ?)",
                       (category, manufacturer, product_name, quantity, price, "BYN"))
        self.connect.commit()

    def dell_product(self):
        self.display_all_products()
        product_id = int(input("Введите ID продукта, который вы хотите удалить: "))
        self.c.execute("DELETE FROM products WHERE product_id = ?;", (product_id,))
        self.connect.commit()
        print(f"Товар с ID {product_id} удален.")
        

class ManufacturerExc(Exception):
    """Класс для обработки ошибок"""

    def __init__(self, message="Недопустимое значение."):
        self.message = message
        super().__init__(self.message)
        

class ProductNameExc(ManufacturerExc):
    def __init__(self, message="Недопустимое значение название продукта"):
        super().__init__(message)
