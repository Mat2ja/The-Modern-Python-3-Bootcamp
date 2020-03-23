# Define Bank Account Below:


class BankAccount():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


accts = BankAccount("Jim")
print(accts.deposit(150.50))
