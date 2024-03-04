from user import User


class Employee(User):
    def __init__(self, username, password):
        super().__init__(username, password)
