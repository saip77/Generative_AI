#Bank Account System 🏦

'''Create a BankAccount class with attributes account_number, balance.
Methods: deposit(amount), withdraw(amount), check_balance().
Prevent withdrawing more than balance (Exception handling).
'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}")

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}")
        else:
            raise Exception("Insufficient funds")
            
    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

account1 = BankAccount("123456789", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()