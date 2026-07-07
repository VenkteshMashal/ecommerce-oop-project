from database.connection import create_tables
from services.product_service import ProductService

if __name__ == "__main__":
    create_tables()

    success, message = ProductService.add_product(
        name="Laptop",
        category="Electronics",
        price=55000,
        stock=10,
        description="Dell business laptop"
    )

    print(message)

    products = ProductService.get_all_products()

    print("\nProducts:")
    for product in products:
        print(
            product["product_id"],
            product["name"],
            product["category"],
            product["price"],
            product["stock"]
        )