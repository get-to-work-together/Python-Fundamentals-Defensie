import math


class Breuk:

    def __init__(self, teller: int, noemer: int = 1):
        self.teller = teller
        self.noemer = noemer

    def __str__(self):
        return f'{self.teller}/{self.noemer}'

    def __repr__(self):
        return f'Breuk({self.teller}, {self.noemer})'

    def __neg__(self):
        return Breuk(-self.teller, self.noemer)

    def __add__(self, other):
        noemer = self.noemer * other.noemer
        teller1 = self.teller * other.noemer
        teller2 = other.teller * self.noemer
        teller = teller1 + teller2
        return Breuk(teller, noemer)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        teller = self.teller * other.teller
        noemer = self.noemer * other.noemer
        return Breuk(teller, noemer)

    def __truediv__(self, other):
        return self * other.inverse()

    def __pow__(self, power):
        return Breuk(self.teller ** power, self.noemer ** power)

    def __float__(self):
        return self.teller / self.noemer

    def __eq__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer == other.teller * noemer

    def __ne__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer != other.teller * noemer

    def __gt__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer > other.teller * noemer

    def __ge__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer >= other.teller * noemer

    def __lt__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer < other.teller * noemer

    def __le__(self, other):
        noemer = self.noemer * other.noemer
        return self.teller * noemer <= other.teller * noemer

    def inverse(self):
        return Breuk(self.noemer, self.teller)

    def copy(self):
        return Breuk(self.teller, self.noemer)

    def simplify(self):
        gcd = math.gcd(self.teller, self.noemer)
        if self.noemer < 0:
            gcd = -gcd
        self.teller //= gcd
        self.noemer //= gcd

    def simplified(self):
        result = self.copy()
        result.simplify()
        return result



# -------------------------------------------

b1 = Breuk(1, 2)
b2 = Breuk(1, 3)

print('b1:', b1)
print('b2:', b2)

print('b1 inverse:', b1.inverse())

print('6/10 simplified:', Breuk(6, 10).simplified())

print('b1 + b2:', b1 + b2)
print('b1 - b2:', b1 - b2)
print('b1 * b2:', b1 * b2)
print('b1 / b2:', b1 / b2)

print('b1 ** 3:', b1 ** 3)

print('-b1:', -b1)

print('-1/-4 simplified:', Breuk(-1, -4).simplified())
