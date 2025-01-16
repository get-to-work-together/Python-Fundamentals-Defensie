
class BankAccount:

    def __init__(self, accountnr, holder, balance = 0):
        self.accountnr = accountnr
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def info(self):
        print(f'Account {self.accountnr} belongs to {self.holder} and has a balance of € {self.balance}')


class SavingsAccount(BankAccount):

    def info(self):
        print(f'SavingsAccount {self.accountnr} - {self.holder} - balance € {self.balance}')



# -------------------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL99ABCD0864536789', 'Peter')
    acc2 = SavingsAccount('NL11DCBA0861111432', 'Lisa', 100)

    acc1.info()
    acc2.info()

    acc1.deposit(1000)
    acc2.deposit(300)
    acc1.withdraw(23)
    acc1.withdraw(23)
    acc1.withdraw(78)
    acc1.withdraw(120)
    acc2.deposit(500)
    acc1.deposit(100)
    acc1.withdraw(267)
    acc2.deposit(1000)
    acc1.withdraw(200)
    acc1.deposit(10)

    acc1.info()
    acc2.info()
