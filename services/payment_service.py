from models.payment import UPIPayment, CardPayment, CashOnDelivery


class PaymentService:

    @staticmethod
    def process_payment(payment_method, amount):
        if payment_method == "UPI":
            payment = UPIPayment(amount)

        elif payment_method == "Card":
            payment = CardPayment(amount)

        elif payment_method == "Cash on Delivery":
            payment = CashOnDelivery(amount)

        else:
            return False, "Invalid payment method."

        return payment.pay()