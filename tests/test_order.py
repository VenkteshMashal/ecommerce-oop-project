from database.connection import create_tables
from services.auth_service import AuthService
from services.product_service import ProductService
from services.cart_service import CartService
from services.order_service import OrderService


def test_order_module():
    create_tables()

    AuthService.register_user(
        name="Order User",
        email="orderuser@example.com",
        password="12345",
        role="customer"
    )

    success, message, user = AuthService.login_user(
        email="orderuser@example.com",
        password="12345"
    )

    print(message)

    ProductService.add_product(
        name="Headphones",
        category="Electronics",
        price=1500,
        stock=10,
        description="Bluetooth headphones"
    )

    products = ProductService.search_products("Headphones")
    product = products[-1]

    CartService.add_to_cart(
        user_id=user["user_id"],
        product_id=product["product_id"],
        quantity=2
    )

    success, message, order_id = OrderService.place_order(
        user_id=user["user_id"],
        payment_method="Cash on Delivery"
    )

    print(message)
    print("Order ID:", order_id)

    print("\nOrder History:")
    orders = OrderService.get_user_orders(user["user_id"])

    for order in orders:
        print(
            order["order_id"],
            order["total_amount"],
            order["payment_method"],
            order["order_status"]
        )

    print("\nOrder Details:")
    details = OrderService.get_order_details(order_id)

    for item in details:
        print(
            item["name"],
            item["quantity"],
            item["price"],
            item["item_total"]
        )


if __name__ == "__main__":
    test_order_module()