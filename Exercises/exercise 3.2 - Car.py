class Car:

    def __init__(self, make, type, color):
        self._make = make
        self._type = type
        self._color = color
        self._mileage = 0

    def get_info(self):
        return f'This great {self._color} {self._make} {self._type} as driven {self._mileage}km.'

    def drive(self, km):
        self._mileage += km

    def __str__(self):
        return f'Car("{self._make}", "{self._type}", "{self._color}", {self._mileage})'

# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown')

    my_car.drive(200)
    my_car.drive(40)

    print(my_car.get_info())
    print(my_car)
