import csv

from account import Account
from client import Client
from employee import Employee


class Repository:
    def __init__(self, clients):
        self.clients = clients

    @staticmethod
    def write_clients(clients):
        with open('clients.csv', 'w', newline='') as csvfile:
            for client in clients:
                row = [client.name, client.username, client.password]
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(row)

    @staticmethod
    def read_clients():
        clients = []
        with open('clients.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                client = Client(row[0], row[1], row[2])
                clients.append(client)
        return clients

    @staticmethod
    def read_employees():
        employees = []
        with open('employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                employee = Employee(row[0], row[1])
                employees.append(employee)
        return employees

    @staticmethod
    def write_accounts(accounts):
        with open('accounts.csv', 'w', newline='') as csvfile:
            for account in accounts:
                row = [account.number, account.amount, account.client]
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(row)

    @staticmethod
    def read_accounts():
        accounts = []
        with open('accounts.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                account = Account(row[0], row[1], row[2])
                accounts.append(account)
        return accounts

    @staticmethod
    def add_client(client):
        with open('clients.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([client.name, client.username, client.password])

    @staticmethod
    def add_account(account):
        with open('accounts.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([account.number, account.amount, account.client.username])
