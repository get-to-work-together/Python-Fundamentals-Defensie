import unittest
from Car import Car

class TestStringMethods(unittest.TestCase):

    def test_km_0(self):
        car = Car('X', 'X', 'X')
        km = car._mileage
        self.assertEqual(0, km)

    def test_km_1(self):
        car = Car('X', 'X', 'X')
        car.drive(197)
        car.drive(23)
        km = car._mileage
        self.assertEqual(220, km)

    def test_km_color(self):
        car = Car('X', 'X', 'bruin')
        kleur = car._color
        self.assertEqual('bruin', kleur)


if __name__ == '__main__':
    unittest.main()

