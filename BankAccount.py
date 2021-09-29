class BankAccount:
    everything = []
    def __init__(self, name):
        self.name = name
        self.int_rate = 0.1
        self.balance = 0
        BankAccount.everything.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee {self.balance - 5}")
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance is: {self.balance}")
        return self

    def yield_interest(self):
        bal_after_int = self.balance * self.int_rate
        self.balance += bal_after_int
        return self

    @classmethod
    def all_accounts(cls):
        for accounts in cls.everything:
            print(accounts.name, accounts.balance)

account1 = BankAccount("account1")
account2 = BankAccount("account2")

account1.deposit(100).deposit(150).deposit(200).withdraw(300).yield_interest().display_account_info()
account2.deposit(500).deposit(1200).withdraw(900).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.all_accounts()
