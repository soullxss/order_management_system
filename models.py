class Customer:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"


class Product:


    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class Order:


    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total = sum(product.price for product in products)

    def __str__(self):
        products_str = ', '.join(str(product) for product in self.products)
        return f"Заказ от {self.customer.name}: {products_str}, Итого: {self.total} руб."
