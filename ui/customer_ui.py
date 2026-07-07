import customtkinter as ctk
from tkinter import messagebox, simpledialog
from utils.theme import Theme
from services.product_service import ProductService
from services.cart_service import CartService


class CustomerDashboard(ctk.CTkToplevel):
    def __init__(self, user):
        super().__init__()

        self.user = user

        self.title("ShopEase - Customer Dashboard")
        self.geometry("900x600")
        self.resizable(False, False)
        self.configure(fg_color=Theme.BG_COLOR)

        self.create_widgets()

    def create_widgets(self):
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=Theme.CARD_COLOR)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        title = ctk.CTkLabel(
            sidebar,
            text="🛒 ShopEase",
            font=("Arial", 24, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        title.pack(pady=(30, 10))

        user_label = ctk.CTkLabel(
            sidebar,
            text=f"Hi, {self.user['name']}",
            font=Theme.FONT_NORMAL,
            text_color=Theme.SUBTEXT_COLOR
        )
        user_label.pack(pady=(0, 30))

        buttons = [
            ("Products", self.show_products),
            ("My Cart", self.show_cart),
            ("My Orders", self.show_orders),
            ("Logout", self.logout)
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                width=170,
                height=40,
                font=Theme.FONT_BUTTON,
                corner_radius=10,
                fg_color=Theme.PRIMARY_COLOR,
                hover_color=Theme.HOVER_COLOR,
                command=command
            )
            btn.pack(pady=10)

        self.content = ctk.CTkFrame(self, fg_color=Theme.BG_COLOR)
        self.content.pack(side="right", fill="both", expand=True)

        self.show_home()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()

        title = ctk.CTkLabel(
            self.content,
            text="Welcome to ShopEase",
            font=("Arial", 30, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        title.pack(pady=(80, 10))

        subtitle = ctk.CTkLabel(
            self.content,
            text="Browse products, add items to cart, and place your order.",
            font=Theme.FONT_SUBTITLE,
            text_color=Theme.SUBTEXT_COLOR
        )
        subtitle.pack(pady=10)

    def show_products(self):
        self.clear_content()

        title = ctk.CTkLabel(
            self.content,
            text="Available Products",
            font=("Arial", 26, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        title.pack(pady=(25, 15))

        products = ProductService.get_all_products()

        if not products:
            label = ctk.CTkLabel(
                self.content,
                text="No products available.",
                font=Theme.FONT_SUBTITLE,
                text_color=Theme.SUBTEXT_COLOR
            )
            label.pack(pady=50)
            return

        scroll_frame = ctk.CTkScrollableFrame(
            self.content,
            width=620,
            height=470,
            fg_color=Theme.BG_COLOR
        )
        scroll_frame.pack(pady=10)

        for product in products:
            card = ctk.CTkFrame(
                scroll_frame,
                width=580,
                height=120,
                corner_radius=12,
                fg_color=Theme.CARD_COLOR
            )
            card.pack(pady=10, padx=10, fill="x")
            card.pack_propagate(False)

            info = ctk.CTkLabel(
                card,
                text=(
                    f"{product['name']}\n"
                    f"Category: {product['category']}\n"
                    f"Price: ₹{product['price']} | Stock: {product['stock']}"
                ),
                font=Theme.FONT_NORMAL,
                text_color=Theme.TEXT_COLOR,
                justify="left"
            )
            info.pack(side="left", padx=20)

            btn = ctk.CTkButton(
                card,
                text="Add to Cart",
                width=130,
                height=38,
                font=Theme.FONT_BUTTON,
                fg_color=Theme.PRIMARY_COLOR,
                hover_color=Theme.HOVER_COLOR,
                command=lambda p_id=product["product_id"]: self.add_product_to_cart(p_id)
            )
            btn.pack(side="right", padx=20)

    def add_product_to_cart(self, product_id):
        quantity = simpledialog.askinteger(
            "Quantity",
            "Enter quantity:",
            minvalue=1
        )

        if quantity is None:
            return

        success, message = CartService.add_to_cart(
            user_id=self.user["user_id"],
            product_id=product_id,
            quantity=quantity
        )

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def show_cart(self):
        self.clear_content()

        label = ctk.CTkLabel(
            self.content,
            text="Cart page coming next",
            font=("Arial", 24, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        label.pack(pady=100)

    def show_orders(self):
        self.clear_content()

        label = ctk.CTkLabel(
            self.content,
            text="Orders page coming next",
            font=("Arial", 24, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        label.pack(pady=100)

    def logout(self):
        self.destroy()
        messagebox.showinfo("Logout", "Logged out successfully.")