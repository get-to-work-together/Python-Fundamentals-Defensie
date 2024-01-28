class Car:

    def __init__(self, make, type, color, mileage = 0):
        self._make = make
        self._type = type
        self._color = color
        self._mileage = mileage

    def get_info(self):
        return f'This great {self._color} {self._make} {self._type} as driven {self._mileage}km.'

    def drive(self, km):
        self._mileage += km

    def __repr__(self):
        return f'Car("{self._make}", "{self._type}", "{self._color}", {self._mileage})'

    def __str__(self):
        return f'Car - {self._color} {self._make} {self._type} - {self._mileage}km'

# -------------------------------------------------------


if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown')

    my_car.drive(200)
    my_car.drive(40)

    print(my_car.get_info())

    print(repr(my_car))
    print(str(my_car))
