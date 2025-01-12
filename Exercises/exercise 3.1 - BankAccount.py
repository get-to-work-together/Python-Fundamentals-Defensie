
class BankAccount:
    """This is my very special BankAccount class"""

    currency = '$'

    __slots__ = ('_holder', '_number', '_balance')

    def __init__(self, number: str, holder: str, balance: int = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount
        else:
            print('Nice try.')

    def deposit(self, amount):
        self._balance += amount

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a saldo of {BankAccount.currency}{self._balance}.'


# ------------------------------------------------------------

acc1 = BankAccount('NL54ABCD0987656432', 'Tammaso', 100)

print(acc1.get_info())

acc1.deposit(1000)
acc1.withdraw(-120)
acc1.withdraw(80)

print(acc1.get_info())

acc2 = BankAccount('NL54ABCD0976766574', 'Diana')
print(acc2.get_info())

acc2.deposit(1000)
acc2.withdraw(900)
acc2.withdraw(80)
acc2.withdraw(2)

print(acc2.get_info())
