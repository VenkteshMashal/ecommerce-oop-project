class CartItem:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cart_total(self):
        return sum(item.get_total_price() for item in self.items)