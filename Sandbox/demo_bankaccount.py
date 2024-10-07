
class BankAccount:

    def __init__(self, account_number, account_holder, currency='€'):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0
        self.__currency = currency

    def __str__(self):
        return 'Account %s of %s has a balance of %s%d' % (self.__account_number,
                                                          self.__account_holder,
                                                          self.__currency,
                                                          self.__balance)

    def __repr__(self):
        return f"BankAccount('{self.__account_number}, '{self.__account_holder}')"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def info(self):
        print('Account %s of %s has a balance of %s%d' % (self.__account_number,
                                                          self.__account_holder,
                                                          self.__currency,
                                                          self.__balance))

# ---------------------

acc1 = BankAccount('NL45ABCD0867645378', 'Nirupam')
acc1.info()

acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(23)

acc1.info()

print(acc1)