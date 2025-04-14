"""
Create a class called BankAccount with:

owner (e.g. name of the person)

balance (default: 0)

Add the following methods:

deposit(amount) – adds amount to balance

withdraw(amount) – subtracts amount if balance is enough, otherwise print "Insufficient funds."

display_balance() – prints "Current balance: [balance]"
"""
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
    def display_balance(self):
        print(f"Current balance: {self.balance}")
        
# Create an instance of BankAccount
account = BankAccount("Dennzy")
Owner = account.owner
print(f"Account owner: {Owner}")
# Display initial balance
balance = account.balance
account.display_balance()
account.deposit(100)
account.display_balance()
account.withdraw(50)
account.display_balance()
account.withdraw(100)
account.display_balance()