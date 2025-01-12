class Car:
    """This is my Car class.

    It simulates driving a car and keeping track of mileage and fuel usage."""

    def __init__(self, make, type, color, mileage = 0, tanksize = 50, usage = 20, tanklevel = 0):
        self._make = make
        self._type = type
        self._color = color
        self._mileage = mileage # km per l
        self._usage = usage
        self._tanksize = tanksize
        self._tanklevel = tanklevel

    def get_info(self):
        info = f'This great {self._color} {self._make} {self._type} as driven {self._mileage}km.\n' + \
               f'The tank has {self._tanklevel}l gasoline.'
        return info

    def drive(self, distance):
        self._mileage += distance
        amount_gasoline = distance / self._usage
        self._tanklevel = max(self._tanklevel + amount_gasoline, 0)

    def __str__(self):
        return f'Car("{self._make}", "{self._type}", "{self._color}", {self._mileage})'

    def __del__(self):
        print('Deze auto is naar de sloop.')

    def __eq__(self, other):
        return self._mileage == other._mileage
    def __ne__(self, other):
        return self._mileage != other._mileage
    def __lt__(self, other):
        return self._mileage < other._mileage
    def __le__(self, other):
        return self._mileage <= other._mileage
    def __gt__(self, other):
        return self._mileage > other._mileage
    def __ge__(self, other):
        return self._mileage >= other._mileage

    def __add__(self, other):
        return self._mileage + other._mileage


    def fill(self, amount_gasoline):
        self._tanklevel = min(self._tanklevel + amount_gasoline, self._tanksize)


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown', 374000)

    my_car.drive(200)

    print(my_car.get_info())
    print(my_car)

    second_car = Car('Opel', 'Kadett', 'zwart', 3000)

    print(second_car.get_info())

    if my_car > second_car:
        print('Mijn auto heeft er meer kilometers op zitten')
    else:
        print('Jouw auto heeft er meer kilometers op zitten')

    samen = my_car + second_car
    print(f'Samen hebben we er {samen} op zitten')
