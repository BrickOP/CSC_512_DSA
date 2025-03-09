class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: Balance is {balance}, but you tried to withdraw {amount}.")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

try:
    alice_account = BankAccount("Alice", 100)
    alice_account.deposit(50)
    alice_account.withdraw(200)
except ValueError as ve:
    print(f"ValueError: {ve}")
except InsufficientFundsError as ife:
    print(f"InsufficientFundsError: {ife}")

try:
    alice_account.withdraw(20)
except ValueError as ve:
    print(f"ValueError: {ve}")
except InsufficientFundsError as ife:
    print(f"InsufficientFundsError: {ife}")
