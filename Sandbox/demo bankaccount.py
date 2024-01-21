import random

class BankAccount:

    CURRENCY = '€'

    def __init__(self, number, holder, balance=0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def __str__(self):
        return f'Bankaccount {self._number} - {self._holder} - saldo {BankAccount.CURRENCY} {self._balance}.'

    def __repr__(self):
        return f'Bankaccount("{self._number}", "{self._holder}", {self._balance})'

    def __gt__(self, other):
        return self._balance > other._balance
    def __ge__(self, other):
        return self._balance >= other._balance
    def __lt__(self, other):
        return self._balance < other._balance
    def __le__(self, other):
        return self._balance <= other._balance
    def __eq__(self, other):
        return self._balance == other._balance
    def __ne__(self, other):
        return self._balance != other._balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} and has a saldo of {BankAccount.CURRENCY} {self._balance}.'

    @staticmethod
    def generate_account(holder):
        number = f'NL12ABCD{random.randint(10000, 99999999):0>10}'
        acc = BankAccount(number, holder)
        return acc


class SavingsAccount(BankAccount):

    def get_info(self):
        return f'Savingsaccount with number {self._number} belongs to {self._holder} and has a saldo of {BankAccount.CURRENCY} {self._balance}.'

    def withdraw(self, amount):
        super().withdraw(amount + 0.1)

# -----------------------------------------------------------------------------

acc1 = BankAccount('NL56ABCD0987676543', 'Robin')
acc2 = BankAccount('NL56ABCD0008767878', 'Robin')

acc3 = BankAccount.generate_account('Sander')

acc4 = SavingsAccount('NL56ABCD098768970', 'Robin')

print( acc1.get_info() )
print( acc2.get_info() )
print( acc3.get_info() )
print( acc4.get_info() )

acc1.deposit(1000)
acc2.deposit(2000)
acc1.withdraw(123)
acc2.deposit(123)
acc2.withdraw(500)
acc1.deposit(300)

acc4.deposit(3000)
acc4.withdraw(500)

acc1.transfer(acc2, 200)

print( acc1.get_info() )
print( acc2.get_info() )
print( acc4.get_info() )

print(str(acc1))
print(str(acc2))
print(str(acc3))

print(repr(acc1))
print(repr(acc2))
print(repr(acc3))

print(acc1 > acc2)
