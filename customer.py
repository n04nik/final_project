from manager import Manager


class Customer(Manager):
    def display_all_products(self):
        return super().display_all_products()
    
    def display_sort_min(self):
        self.c.execute("SELECT product_id, category, manufacturer, product_name, quantity, price, currency FROM products ORDER BY price ASC;")
        products = self.c.fetchall()
        for product in products:
            print(product)
            