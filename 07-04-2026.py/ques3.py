#bank account simulator
class BankAccount:
    total_accounts = 0

    def __init__(self, holder, balance):
        self.account_holder = holder
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Balance:", self.balance)


# Test
acc = BankAccount("John", 1000)

acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)

acc.display_balance()

print("Total Accounts:", BankAccount.total_accounts)