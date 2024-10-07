import re


class BankAccount:
    """This is my BankAccount class"""

    currency = '$'

    __slots__ = ('_number','_holder','_balance')

    def __init__(self, number, holder, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def __del__(self):
        print('Account has been closed.')

    def __str__(self):
        return f'Bankaccount {self._number} - saldo of {BankAccount.currency} {self._balance}.'

    def __repr__(self):
        return f'BankAccount("{self._number}", "{self._holder}", {self._balance})'

    def __eq__(self, other):
        return self._balance == other._balance
    def __ne__(self, other):
        return self._balance != other._balance
    def __gt__(self, other):
        return self._balance > other._balance
    def __ge__(self, other):
        return self._balance >= other._balance
    def __lt__(self, other):
        return self._balance < other._balance
    def __le__(self, other):
        return self._balance <= other._balance

    def __add__(self, other):
        return self._balance + other._balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        print(f'Withdraw of {BankAccount.currency} {amount}')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of {BankAccount.currency} {amount}')

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a saldo of {BankAccount.currency} {self._balance}.'




class SavingsAccount(BankAccount):

    def __str__(self):
        return f'Savings account {self._number} - saldo of {BankAccount.currency} {self._balance}.'

    def __repr__(self):
        return f'SavingsAccount("{self._number}", "{self._holder}", {self._balance})'

    def get_info(self):
        return f'Savings account with number {self._number} belongs to {self._holder} has a saldo of {BankAccount.currency} {self._balance}.'


    # def __init__(self, number, holder, balance = 0, interest = 0.01):
    #     super().__init__(number, holder, balance)
    #     self._interest = interest
    #
    # def add_interest(self):
    #     self._balance += self._balance * self._interest



class Person:

    def __init__(self, name):
        self._name = name
        self._accounts = {}    # bankaccount or savingsaccount

    def add_account(self, account, account_name):
        self._accounts[account_name] = account

    def get_account(self, account_name):
        return self._accounts[account_name]



# ------------------------------------------------------------

person = Person('Joey')



acc1 = BankAccount('NL54ABCD09876564324', 'Joey Betaalrekening')

person.add_account(BankAccount('NL54ABCD09876564324', 'Joey'), 'Betaalrekening')


acc1.deposit(1000)
acc1.withdraw(120)
acc1.withdraw(80)

print(acc1.get_info())

acc2 = BankAccount('NL54ABCD0976766574', 'Joey Vakantie')

acc2.deposit(1000)
acc2.withdraw(900)
acc2.withdraw(80)
acc2.withdraw(2)

print(acc2.get_info())

if acc1.balance > acc2.balance:
    print("acc1 has a larger balance than account2")


    
acc3 = SavingsAccount('NL7877686876876', 'Joey Spaar')

acc3.deposit(1000)
acc3.deposit(1000)
acc3.deposit(1000)
acc3.deposit(1000)

# acc3.add_interest()

print(acc3.get_info())

