from account import Account
from repository import Repository
from client import Client
import uuid


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.employees = []

    def register_client(self, name, username, password, initial_amount):
        for client in self.clients:
            if username == client.username:
                return False

        for employee in self.employees:
            if username == employee.username:
                return False

        client = Client(name, username, password)
        account = Account(uuid.uuid4(), initial_amount, client)

        account.client = client
        client.accounts.append(account)

        self.clients.append(client)

        Repository.add_client(client)
        Repository.add_account(account)
        return True

    def authenticate(self, username, password):
        for client in self.clients:
            if username == client.username and password == client.password:
                return client

        for employee in self.employees:
            if username == employee.username and password == employee.password:
                return employee

    def delete_client(self, username):
        for client in self.clients:
            if username == client.username:
                self.clients.remove(client)
                accounts = Repository.read_accounts()
                for account in accounts:
                    if account.client == username:
                        accounts.remove(account)
                Repository.write_clients(self.clients)
                Repository.write_accounts(accounts)
                return True
        return False
