class Product:
    def __init__(self, name, category, price, stock, description=""):
        self.name = name
        self.category = category
        self.__price = price
        self.__stock = stock
        self.description = description

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self.__stock:
            raise ValueError("Not enough stock available.")

        self.__stock -= quantity

    def increase_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.__stock += quantity