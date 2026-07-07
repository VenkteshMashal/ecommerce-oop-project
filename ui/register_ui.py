import customtkinter as ctk
from tkinter import messagebox
from services.auth_service import AuthService


class RegisterUI(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("ShopEase - Register")
        self.geometry("420x560")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Register as a customer",
            font=("Arial", 15)
        )
        subtitle.pack(pady=(0, 25))

        self.name_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Enter Name"
        )
        self.name_entry.pack(pady=10)

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

        self.confirm_password_entry = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Confirm Password",
            show="*"
        )
        self.confirm_password_entry.pack(pady=10)

        register_btn = ctk.CTkButton(
            self,
            text="Create Account",
            width=300,
            height=40,
            command=self.register
        )
        register_btn.pack(pady=25)

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

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