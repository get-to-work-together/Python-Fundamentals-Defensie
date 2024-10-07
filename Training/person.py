
class Person:

    def __init__(self, name: str, residence: str):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'Ik ben {self.name} en ik woon in {self.residence}.')

    def move(self, new_residence: str):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name: str, residence: str, customernr: str):
        super().__init__(name, residence)
        self.customernr = customernr

    def tell(self):
        print(f'Ik ben {self.name} ({self.customernr}) en ik woon in {self.residence}.')


# ------------------------------------------

# instantie
p1 = Person('Peter', 'Lhee')
p2 = Customer('Dave', 'Arnhem', 'VIP007')

# methodes
p1.tell()
p1.move('Soesterberg')
p1.tell()
p1.move('Utrecht')
p1.tell()

p2.move('Soesterberg')
p2.tell()