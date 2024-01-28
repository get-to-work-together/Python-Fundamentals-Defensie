
class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'Ik ben {self.name} en ik woon in {self.residence}.'

    def move(self, new_residence):
        self.residence = new_residence


# --------------------------------------------------

p1 = Person('Peter', 'Lhee')
p2 = Person('Maurice', 'Harderwijk')

print(p1.tell())
print(p2.tell())

p1.move('Soesterberg')
print(p1.tell())
