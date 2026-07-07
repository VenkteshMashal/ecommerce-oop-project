from services.payment_service import PaymentService


def test_payment_module():
    methods = ["UPI", "Card", "Cash on Delivery"]

    for method in methods:
        success, message = PaymentService.process_payment(method, 2500)
        print(message)


if __name__ == "__main__":
    test_payment_module()