from database.connection import get_connection
from models.product import Product


class ProductService:

    @staticmethod
    def add_product(name, category, price, stock, description=""):
        if not name or not category:
            return False, "Product name and category are required."

        if price <= 0:
            return False, "Price must be greater than zero."

        if stock < 0:
            return False, "Stock cannot be negative."

        product = Product(name, category, price, stock, description)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO products (name, category, price, stock, description)
            VALUES (?, ?, ?, ?, ?)
        """, (
            product.name,
            product.category,
            product.get_price(),
            product.get_stock(),
            product.description
        ))

        conn.commit()
        conn.close()

        return True, "Product added successfully."

    @staticmethod
    def get_all_products():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        conn.close()
        return products

    @staticmethod
    def get_product_by_id(product_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        conn.close()
        return product

    @staticmethod
    def update_product(product_id, name, category, price, stock, description=""):
        if price <= 0:
            return False, "Price must be greater than zero."

        if stock < 0:
            return False, "Stock cannot be negative."

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE products
            SET name = ?, category = ?, price = ?, stock = ?, description = ?
            WHERE product_id = ?
        """, (name, category, price, stock, description, product_id))

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        if updated == 0:
            return False, "Product not found."

        return True, "Product updated successfully."

    @staticmethod
    def delete_product(product_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted == 0:
            return False, "Product not found."

        return True, "Product deleted successfully."

    @staticmethod
    def search_products(keyword):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM products
            WHERE name LIKE ? OR category LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        products = cursor.fetchall()

        conn.close()
        return products