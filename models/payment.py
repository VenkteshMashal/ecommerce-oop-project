from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):
    def pay(self):
        return True, f"UPI payment of ₹{self.amount} successful."


class CardPayment(Payment):
    def pay(self):
        return True, f"Card payment of ₹{self.amount} successful."


class CashOnDelivery(Payment):
    def pay(self):
        return True, f"Cash on Delivery selected for ₹{self.amount}."