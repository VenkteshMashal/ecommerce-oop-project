from database.connection import create_tables
from services.product_service import ProductService


def test_product_module():
    create_tables()

    print("\nAdding product...")
    success, message = ProductService.add_product(
        name="Keyboard",
        category="Electronics",
        price=1200,
        stock=15,
        description="Mechanical keyboard"
    )
    print(message)

    print("\nAll products:")
    products = ProductService.get_all_products()

    for product in products:
        print(
            product["product_id"],
            product["name"],
            product["category"],
            product["price"],
            product["stock"]
        )


if __name__ == "__main__":
    test_product_module()