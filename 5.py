class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance += amount
        return self.balance

account=BankAccount()
print(account.deposit(100))