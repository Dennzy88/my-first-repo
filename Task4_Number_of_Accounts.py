"""
Enhance your BankAccount class with:

Class variable:
account_count → keeps track of how many accounts have been created

Class method:
get_account_count() → returns the number of accounts created
"""
class BankAccount:
    account_count = 0
    
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        BankAccount.account_count += 1
        
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
        
    @classmethod
    def get_account_count(cls):
        return cls.account_count
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"  
    
# Create instances of BankAccount
account1 = BankAccount("Dennzy")
account2 = BankAccount("Alice")
account3 = BankAccount("Bob")
print(account1)
print(account2)
print(account3)

# Display the number of accounts created
account_count = BankAccount.get_account_count() 
print(f"Number of accounts created: {account_count}")

