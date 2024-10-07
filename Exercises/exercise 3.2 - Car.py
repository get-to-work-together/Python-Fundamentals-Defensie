class Car:

    def __init__(self, make: str, model: str, color: str, mileage: int = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def __str__(self):
        return f'This {self._color} {self._make} {self._model} as driven {self._mileage}km.'

    def __repr__(self):
        return f'Car("{self._make}", "{self._model}", "{self._color}", {self._mileage})'

    def get_info(self) -> str:
        return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.'

    def drive(self, km: int):
        self._mileage += km

# -------------------------------------------------------


if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown', 460000)
    your_car = Car('Peugout', '200', 'red', 46000)

    my_car.drive(170)
    my_car.drive(170)

    print(my_car.get_info())
