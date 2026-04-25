#E-commerce product catalog
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price}"


class Electronics(Product):
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price} (Electronics, Warranty: {self.warranty} months)"


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price} (Clothing, Size: {self.size})"


class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        print("--- Product Catalog ---")
        for product in self.products:
            print(product)


# Test
catalog = Catalog()

catalog.add_product(Electronics("E101", "Laptop", 1200, 24))
catalog.add_product(Clothing("C101", "T-Shirt", 25, "L"))

catalog.display_all_products()