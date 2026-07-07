from database.connection import create_tables
from services.auth_service import AuthService
from services.product_service import ProductService
from services.cart_service import CartService


def test_cart_module():
    create_tables()

    AuthService.register_user(
        name="Cart User",
        email="cartuser@example.com",
        password="12345",
        role="customer"
    )

    success, message, user = AuthService.login_user(
        email="cartuser@example.com",
        password="12345"
    )

    print(message)

    ProductService.add_product(
        name="Mouse",
        category="Electronics",
        price=700,
        stock=20,
        description="Wireless mouse"
    )

    products = ProductService.search_products("Mouse")
    product = products[-1]

    success, message = CartService.add_to_cart(
        user_id=user["user_id"],
        product_id=product["product_id"],
        quantity=2
    )

    print(message)

    print("\nCart Items:")
    cart_items = CartService.get_cart_items(user["user_id"])

    for item in cart_items:
        print(
            item["name"],
            item["price"],
            item["quantity"],
            item["total_price"]
        )

    print("\nCart Total:", CartService.get_cart_total(user["user_id"]))


if __name__ == "__main__":
    test_cart_module()