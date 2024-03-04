class Account:
    def __init__(self, number, amount, client):
        self.number = number
        self.amount = amount
        self.client = client

    def __repr__(self):
        return '%-*s%-*s' % (40, self.number, 40, self.amount)
