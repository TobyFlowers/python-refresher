# Create a simulation of a bank account.

# The account should have a balance, a name and an account number.
# The account should have a method to withdraw money.
# The account should have a method to deposit money.
# The account should have a method to print the current balance.


class Account:
    def __init__(self, name, account_number, balance=0):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, amount):
        amount = abs(amount)
        if amount > self.balance:
            raise ValueError("Not enough money in account!")
        else:
            self.balance -= amount

    def deposit(self, amount):
        amount = abs(amount)
        self.balance += amount

    def client_balance(self):
        return self.balance
