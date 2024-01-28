
class BankAccount:

    currency = '$'

    def __init__(self, accountnr, holder, balance = 0):
        self._accountnr = accountnr
        self._holder = holder
        self._balance = balance

    def info(self):
        return f'Er staat nog {BankAccount.currency}{self._balance} op rekening {self._accountnr} van {self._holder}.'

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @staticmethod
    def change_currency(new_currency):
        BankAccount.currency = new_currency


class SavingsAccount(BankAccount):

    def __init__(self, accountnr, holder, balance = 0, rente = 0.0):
        super().__init__(accountnr, holder, balance)
        self._rente = rente

    def info(self):
        return f'Je hebt al {BankAccount.currency}{self._balance} gespaard op rekening {self._accountnr}.'



# --------------------------------------------------

acc1 = BankAccount('NL99ABCD0123457388', 'Peter')

print(acc1.info())
acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(22)
print(acc1.info())


acc2 = SavingsAccount('NL99ABCD0123457388', 'Peter', 0.8)

print(acc2.info())
acc2.deposit(10000)
print(acc2.info())
