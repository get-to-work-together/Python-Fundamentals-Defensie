
class BankAccount:
    """This is my BankAccount class"""

    __slots__ = ('_number','_holder','_balance')

    def __init__(self, number, holder, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def withdraw(self, amount):
        self._balance = self._balance - amount
        print(f'Withdraw of {BankAccount.currency} {amount}')

    def deposit(self, amount):
        self._balance = self._balance + amount
        print(f'Deposit of {BankAccount.currency} {amount}')

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a saldo of {BankAccount.currency} {self._balance}.'

# ------------------------------------------------------------

acc1 = BankAccount('NL54ABCD09876564324', 'Tammaso')

acc1.deposit(1000)
acc1.withdraw(120)
acc1.withdraw(80)

print(acc1.get_info())

acc2 = BankAccount('NL54ABCD0976766574', 'Diana')

acc2.deposit(1000)
acc2.withdraw(900)
acc2.withdraw(80)
acc2.withdraw(2)

print(acc2.get_info())
