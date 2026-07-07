import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import AuthService
from ui.register_ui import RegisterUI
from utils.theme import Theme
from ui.customer_ui import CustomerDashboard

class LoginUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        Theme.apply_theme()

        self.title("ShopEase - Login")
        self.geometry(f"{Theme.WINDOW_WIDTH}x{Theme.WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.configure(fg_color=Theme.BG_COLOR)

        self.create_widgets()

    def create_widgets(self):
        card = ctk.CTkFrame(
            self,
            width=380,
            height=460,
            corner_radius=18,
            fg_color=Theme.CARD_COLOR
        )
        card.pack(pady=45)
        card.pack_propagate(False)

        title = ctk.CTkLabel(
            card,
            text="🛒 ShopEase",
            font=Theme.FONT_TITLE,
            text_color=Theme.TEXT_COLOR
        )
        title.pack(pady=(40, 8))

        subtitle = ctk.CTkLabel(
            card,
            text="Welcome back! Login to continue",
            font=Theme.FONT_SUBTITLE,
            text_color=Theme.SUBTEXT_COLOR
        )
        subtitle.pack(pady=(0, 30))

        self.email_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Email Address",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Password",
            show="*",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.password_entry.pack(pady=10)

        login_btn = ctk.CTkButton(
            card,
            text="Login",
            width=300,
            height=42,
            font=Theme.FONT_BUTTON,
            corner_radius=10,
            fg_color=Theme.PRIMARY_COLOR,
            hover_color=Theme.HOVER_COLOR,
            command=self.login
        )
        login_btn.pack(pady=(25, 12))

        register_btn = ctk.CTkButton(
            card,
            text="Create New Account",
            width=300,
            height=42,
            font=Theme.FONT_BUTTON,
            corner_radius=10,
            fg_color="transparent",
            border_width=1,
            border_color=Theme.PRIMARY_COLOR,
            hover_color=Theme.HOVER_COLOR,
            command=self.open_register_window
        )
        register_btn.pack(pady=5)

    def open_register_window(self):
        RegisterUI()

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Email and password are required.")
            return

        success, message, user = AuthService.login_user(email, password)

        if success:
            messagebox.showinfo("Success", f"Welcome {user['name']}")

            if user["role"] == "customer":
                CustomerDashboard(user)
            else:
                messagebox.showinfo("Admin", "Admin dashboard coming soon.")
        else:
            messagebox.showerror("Login Failed", message)