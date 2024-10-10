class Bankaccount:

    def __init__(self, account_number: str, holder: str, balance: float|int = 0.0):
        self._account_number = account_number
        self._holder = holder
        self._balance = balance

    def deposit(self, amount: float|int):
        self._balance += amount

    def withdraw(self, amount: float|int):
        self._balance -= amount

    def transfer(self, destination, amount: float|int):
        self.withdraw(amount)
        destination.deposit(amount)

    def info(self):
        return f'Account {self._account_number} belonging to {self._holder} has a balance of €{self._balance:.2f}'


# ---------------------------------------------------------------------------------------------

if __name__ == '__main__':

    acc1 = Bankaccount('NL99ABCD9123443256', 'Peter', 998)
    acc2 = Bankaccount('NL99ABCD9123443265', 'Chris')

    print(acc1.info())
    print(acc2.info())

    acc1.deposit(1000)
    acc1.withdraw(23)
    acc1.withdraw(65)

    print(acc1.info())

    acc1.transfer(acc2, 333)

    print(acc1.info())
    print(acc2.info())

    print(dir(acc1))


