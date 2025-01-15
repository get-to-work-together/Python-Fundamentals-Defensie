
class Person:

    # initialize van attributes
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'Ik ben {self.name} en ik woon in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence


# ------------------------------------------------

p1 = Person('Peter', 'Lhee')
p2 = Person('Marc', 'Stroe')
p3 = Person('Lindsey', 'Zeist')


p1.tell()
p1.move('Soesterberg')
p1.tell()

p2.tell()
p3.tell()