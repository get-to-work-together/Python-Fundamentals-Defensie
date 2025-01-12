class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'I am {self.name} from {self.residence}'

    def move(self, new_residence):
        self.residence = new_residence


# ------------------------------------------------------------

p1 = Person('Albert','Amsterdam')
p2 = Person('Susan','Utrecht')

print( p2.tell() )

p2.move('Rotterdam')

print( p2.tell() )
