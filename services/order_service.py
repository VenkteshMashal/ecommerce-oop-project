from database.connection import get_connection
from services.cart_service import CartService
from models.order import Order
from services.payment_service import PaymentService

class OrderService:

    @staticmethod
    def place_order(user_id, payment_method):
        cart_items = CartService.get_cart_items(user_id)
        
        if not cart_items:
            return False, "Cart is empty.", None

        total_amount = CartService.get_cart_total(user_id)
        payment_success, payment_message = PaymentService.process_payment(
            payment_method,
            total_amount
        )

        if not payment_success:
            return False, payment_message, None

        order = Order(user_id, total_amount, payment_method)

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO orders (user_id, total_amount, payment_method, order_status)
                VALUES (?, ?, ?, ?)
            """, (
                order.user_id,
                order.total_amount,
                order.payment_method,
                order.status
            ))

            order_id = cursor.lastrowid

            for item in cart_items:
                product_id = item["product_id"]
                quantity = item["quantity"]
                price = item["price"]

                cursor.execute("""
                    INSERT INTO order_items (order_id, product_id, quantity, price)
                    VALUES (?, ?, ?, ?)
                """, (order_id, product_id, quantity, price))

                cursor.execute("""
                    UPDATE products
                    SET stock = stock - ?
                    WHERE product_id = ?
                """, (quantity, product_id))

            cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))

            conn.commit()
            return True, "Order placed successfully.", order_id

        except Exception as e:
            conn.rollback()
            return False, f"Order failed: {e}", None

        finally:
            conn.close()

    @staticmethod
    def get_user_orders(user_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM orders
            WHERE user_id = ?
            ORDER BY created_at DESC
        """, (user_id,))

        orders = cursor.fetchall()
        conn.close()

        return orders

    @staticmethod
    def get_order_details(order_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                orders.order_id,
                orders.total_amount,
                orders.payment_method,
                orders.order_status,
                orders.created_at,
                products.name,
                order_items.quantity,
                order_items.price,
                (order_items.quantity * order_items.price) AS item_total
            FROM order_items
            JOIN orders ON order_items.order_id = orders.order_id
            JOIN products ON order_items.product_id = products.product_id
            WHERE orders.order_id = ?
        """, (order_id,))

        items = cursor.fetchall()
        conn.close()

        return items