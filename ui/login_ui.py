import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import AuthService


class LoginUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ShopEase - Login")
        self.geometry("420x500")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="ShopEase",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=(50, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Login to your account",
            font=("Arial", 16)
        )
        subtitle.pack(pady=(0, 30))

        self.email_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Enter Email"
        )
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Enter Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        login_btn = ctk.CTkButton(
            self,
            text="Login",
            width=300,
            height=40,
            command=self.login
        )
        login_btn.pack(pady=25)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Email and password are required.")
            return

        success, message, user = AuthService.login_user(email, password)

        if success:
            messagebox.showinfo("Success", f"Welcome {user['name']}")
            print(user)
        else:
            messagebox.showerror("Login Failed", message)