import bcrypt
from database.connection import get_connection
from models.user import Customer, Admin


class AuthService:

    @staticmethod
    def hash_password(password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password, hashed_password):
        password_bytes = password.encode("utf-8")
        hashed_bytes = hashed_password.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    @staticmethod
    def register_user(name, email, password, role="customer"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return False, "Email already registered."

        hashed_password = AuthService.hash_password(password)

        if role == "admin":
            user = Admin(name, email, hashed_password)
        else:
            user = Customer(name, email, hashed_password)

        cursor.execute("""
            INSERT INTO users (name, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (
            user.name,
            user.email,
            user.get_password(),
            user.role
        ))

        conn.commit()
        conn.close()

        return True, "Registration successful."

    @staticmethod
    def login_user(email, password):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        conn.close()

        if not user:
            return False, "User not found.", None

        is_valid = AuthService.verify_password(password, user["password"])

        if not is_valid:
            return False, "Invalid password.", None

        logged_in_user = {
            "user_id": user["user_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }

        return True, "Login successful.", logged_in_user