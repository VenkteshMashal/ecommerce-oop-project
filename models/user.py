class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.__password = password
        self.role = role

    def get_password(self):
        return self.__password


class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, "customer")


class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, "admin")