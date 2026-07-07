from database.connection import get_connection


class CartService:

    @staticmethod
    def add_to_cart(user_id, product_id, quantity):
        if quantity <= 0:
            return False, "Quantity must be greater than zero."

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            conn.close()
            return False, "Product not found."

        if product["stock"] < quantity:
            conn.close()
            return False, "Not enough stock available."

        cursor.execute("""
            SELECT * FROM cart
            WHERE user_id = ? AND product_id = ?
        """, (user_id, product_id))

        existing_item = cursor.fetchone()

        if existing_item:
            new_quantity = existing_item["quantity"] + quantity

            if product["stock"] < new_quantity:
                conn.close()
                return False, "Not enough stock available."

            cursor.execute("""
                UPDATE cart
                SET quantity = ?
                WHERE user_id = ? AND product_id = ?
            """, (new_quantity, user_id, product_id))
        else:
            cursor.execute("""
                INSERT INTO cart (user_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (user_id, product_id, quantity))

        conn.commit()
        conn.close()

        return True, "Product added to cart."

    @staticmethod
    def get_cart_items(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                cart.cart_id,
                products.product_id,
                products.name,
                products.category,
                products.price,
                cart.quantity,
                (products.price * cart.quantity) AS total_price
            FROM cart
            JOIN products ON cart.product_id = products.product_id
            WHERE cart.user_id = ?
        """, (user_id,))

        items = cursor.fetchall()
        conn.close()

        return items

    @staticmethod
    def update_cart_quantity(user_id, product_id, quantity):
        if quantity <= 0:
            return False, "Quantity must be greater than zero."

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT stock FROM products WHERE product_id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            conn.close()
            return False, "Product not found."

        if product["stock"] < quantity:
            conn.close()
            return False, "Not enough stock available."

        cursor.execute("""
            UPDATE cart
            SET quantity = ?
            WHERE user_id = ? AND product_id = ?
        """, (quantity, user_id, product_id))

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        if updated == 0:
            return False, "Cart item not found."

        return True, "Cart quantity updated."

    @staticmethod
    def remove_from_cart(user_id, product_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM cart
            WHERE user_id = ? AND product_id = ?
        """, (user_id, product_id))

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted == 0:
            return False, "Cart item not found."

        return True, "Product removed from cart."

    @staticmethod
    def clear_cart(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))

        conn.commit()
        conn.close()

        return True, "Cart cleared."

    @staticmethod
    def get_cart_total(user_id):
        items = CartService.get_cart_items(user_id)
        return sum(item["total_price"] for item in items)