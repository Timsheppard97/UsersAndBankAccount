import BankAccount

class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount.BankAccount("checking")

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def transfer_money(self, other, amount):
        self.account.balance -= amount
        other.account.balance += amount
        return self

jeff = User("Jeff")
caroline = User("Caroline")
george = User("George")

jeff.make_deposit(100).make_deposit(100).make_deposit(250).display_user_balance()

caroline.make_deposit(1000).make_deposit(375).make_withdrawal(500).make_withdrawal(600).display_user_balance()

george.make_deposit(1250).make_withdrawal(1000).make_withdrawal(100).make_withdrawal(250).display_user_balance()

jeff.transfer_money(caroline,1000).display_user_balance()
caroline.display_user_balance()