
class Car:

    def __init__(self, make: str, model: str, color: str, mileage: int = 0):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

    def info(self):
        print(f'This great {self.color} {self.make} {self.model} has driven {self.mileage}km.')

    def drive(self, distance: int):
        self.mileage += distance


# -------------------------------------------------------------

if __name__ == '__main__':

    car1 = Car('Renault', 'Megane station', 'metalic brown', 485000)

    car1.info()
    car1.drive(180)
    car1.info()
