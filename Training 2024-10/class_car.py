
class Car:

    # class-wide attributes
    distance_unit = 'miles'

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def __del__(self):
        print('Your car has been demolished!')

    def __repr__(self):
        return f'Car("{self._color}", "{self._make}", "{self._model}", {self._mileage})'

    def __str__(self):
        return f'Car: {self._color}, {self._make}, {self._model}, {self._mileage}km'

    def __gt__(self, other):
        return self._mileage > other._mileage
    def __ge__(self, other):
        return self._mileage >= other._mileage
    def __lt__(self, other):
        return self._mileage < other._mileage
    def __le__(self, other):
        return self._mileage <= other._mileage
    def __eq__(self, other):
        return self._mileage == other._mileage
    def __ne__(self, other):
        return self._mileage != other._mileage

    def drive(self, distance):
        if distance > 0:
            self._mileage += distance

    def info(self):
        return f'This beautiful {self._color} {self._make} {self._model} has a mileage of {self._mileage} {Car.distance_unit}.'


# ------------------------------------------------------------------------------

if __name__ == '__main__':

    car1 = Car('Renault', 'Megane Station', 'brown', 474500)

    print(car1.info())

    car1.drive(175)
    car1.drive(175)

    print(car1.info())

    print(str(car1))
    print(repr(car1))

    car2 = Car('Opel', 'Kadett', 'red', 524356)
    print(car2.info())