import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import AuthService
from utils.theme import Theme


class RegisterUI(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("ShopEase - Register")
        self.geometry(f"{Theme.WINDOW_WIDTH}x{Theme.WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.configure(fg_color=Theme.BG_COLOR)

        self.create_widgets()

    def create_widgets(self):
        card = ctk.CTkFrame(
            self,
            width=380,
            height=500,
            corner_radius=18,
            fg_color=Theme.CARD_COLOR
        )
        card.pack(pady=30)
        card.pack_propagate(False)

        title = ctk.CTkLabel(
            card,
            text="Create Account",
            font=("Arial", 28, "bold"),
            text_color=Theme.TEXT_COLOR
        )
        title.pack(pady=(35, 8))

        subtitle = ctk.CTkLabel(
            card,
            text="Register as a customer",
            font=Theme.FONT_SUBTITLE,
            text_color=Theme.SUBTEXT_COLOR
        )
        subtitle.pack(pady=(0, 25))

        self.name_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Full Name",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.name_entry.pack(pady=8)

        self.email_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Email Address",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.email_entry.pack(pady=8)

        self.password_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Password",
            show="*",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.password_entry.pack(pady=8)

        self.confirm_password_entry = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Confirm Password",
            show="*",
            font=Theme.FONT_NORMAL,
            corner_radius=10
        )
        self.confirm_password_entry.pack(pady=8)

        register_btn = ctk.CTkButton(
            card,
            text="Create Account",
            width=300,
            height=42,
            font=Theme.FONT_BUTTON,
            corner_radius=10,
            fg_color=Theme.PRIMARY_COLOR,
            hover_color=Theme.HOVER_COLOR,
            command=self.register
        )
        register_btn.pack(pady=(25, 8))

    def register(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not name or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        success, message = AuthService.register_user(
            name=name,
            email=email,
            password=password,
            role="customer"
        )

        if success:
            messagebox.showinfo("Success", message)
            self.destroy()
        else:
            messagebox.showerror("Registration Failed", message)