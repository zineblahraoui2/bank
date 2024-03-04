from bank import Bank
from client import Client
from employee import Employee
from repository import Repository

bankIAV = Bank('IAV')


def init():
    accounts = Repository.read_accounts()
    clients = Repository.read_clients()
    bankIAV.employees = Repository.read_employees()

    client_accounts = {}

    for account in accounts:
        client_accounts.setdefault(account.client, []).append(account)

    for client in clients:
        client.accounts = client_accounts[client.username]

    bankIAV.clients = clients


init()


def authenticate():
    username = input('Username: ')
    password = input('Password: ')
    return bankIAV.authenticate(username, password)


def employee_menu():
    print('\n1. List clients')
    print('2. Register client')
    print('3. Delete client')
    print('4. Quit')


def list_clients():
    if len(bankIAV.clients) == 0:
        print('No clients!')
    else:
        print('\n%-*s%-*s%-*s%-*s' % (25, 'name', 25, 'username', 40, 'account', 25, 'amount'))
        for client in bankIAV.clients:
            print(client)


def register_client():
    name = input('\nClient name: ')
    username = input('Client username: ')
    password = input('Client password: ')
    initial_amount = int(input('Initial amount: '))

    if bankIAV.register_client(name, username, password, initial_amount):
        print('\nClient registered successfully!')
    else:
        print('\nUsername is already taken!')


def delete_client():
    username = input('Client username: ')
    if bankIAV.delete_client(username):
        print('\nClient deleted successfully!')
    else:
        print('\nClient is not registered!')


def client_menu():
    print('\n1. Account details')
    print('2. Transfer')
    print('3. Quit')


def account_details():
    print('\n%-*s%-*s' % (40, 'account', 40, 'amount'))
    for account in user.accounts:
        print(account)


def quit():
    print('Take care!')
    exit(0)


def invalid_choice():
    print('\nInvalid choice!')


def transfer():
    number = input('\nEnter account number: ')
    amount = float(input('Enter amount to transfer: '))
    from_account = None
    to_account = None
    accounts = Repository.read_accounts()
    for account in accounts:
        if account.number == number:
            to_account = account
        if account.number == user.accounts[0].number:
            from_account = account
        if from_account is not None and to_account is not None:
            break
    if to_account is None:
        print('\nAccount not found!')
    elif from_account.number == to_account.number:
        print('\nYour can\'t transfer money to yourself!')
    elif amount > float(from_account.amount):
        print('\nYou don\'t have enough money!')
    elif amount == 0:
        print('\nYou can\'t transfer nothing!')
    else:
        to_account.amount = float(to_account.amount) + amount
        from_account.amount = float(from_account.amount) - amount
        Repository.write_accounts(accounts)
        print('\nYour transfer was successful!')


user = authenticate()

if user is None:
    print('\nInvalid username or password!')

if isinstance(user, Employee):
    while True:
        employee_menu()
        choice = int(input('\nEnter your choice: '))
        match choice:
            case 1:
                list_clients()
            case 2:
                register_client()
            case 3:
                delete_client()
            case 4:
                quit()
                break
            case _:
                invalid_choice()

elif isinstance(user, Client):
    while True:
        client_menu()
        choice = int(input('\nEnter your choice: '))
        match choice:
            case 1:
                account_details()
            case 2:
                transfer()
            case 3:
                quit()
                break
            case _:
                invalid_choice()
