from user import User


class Client(User):
    def __init__(self, name, username, password):
        super().__init__(username, password)
        self.name = name
        self.accounts = []

    def __repr__(self):
        return '%-*s%-*s%-*s%-*s' % (
            25, self.name, 25, self.username, 40, self.accounts[0].number, 25, self.accounts[0].amount)
