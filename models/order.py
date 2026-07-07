class Order:
    def __init__(self, user_id, total_amount, payment_method):
        self.user_id = user_id
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.status = "Placed"


class OrderItem:
    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price