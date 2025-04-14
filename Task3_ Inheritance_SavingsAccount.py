"""
Create a new class called SavingsAccount that inherits from BankAccount.

Requirements:
Inherits everything from BankAccount

Override the withdraw() method:

If amount > 100, print: "Withdrawal limit exceeded. Max: 100"

Otherwise, perform normal withdrawal only if balance allows
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
        
class SavingsAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.withdrawal_limit = 100
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal limit exceeded. Max: {self.withdrawal_limit}")
        else:
            super().withdraw(amount)
            
# Create an instance of SavingsAccount
savings_account = SavingsAccount("Dennzy")
Owner = savings_account.owner
print(f"Account owner: {Owner}")
# Display initial balance
deposit = savings_account.deposit(200)
savings_account.display_balance()
savings_account.withdraw(50)
savings_account.display_balance()
savings_account.withdraw(150)
savings_account.display_balance()






        


        
    