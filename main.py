from database.connection import create_tables
from services.auth_service import AuthService

if __name__ == "__main__":
    create_tables()

    print("\n1. Register")
    success, message = AuthService.register_user(
        name="Venktesh",
        email="venktesh@example.com",
        password="12345",
        role="customer"
    )
    print(message)

    print("\n2. Login")
    success, message, user = AuthService.login_user(
        email="venktesh@example.com",
        password="12345"
    )

    print(message)
    print(user)