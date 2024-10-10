

class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        return f'Ik ben {self.name} en ik woon in {self.residence}'

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customer_nr):
        super().__init__(name, residence)
        self.customer_nr = customer_nr

    def tell(self):
        return f'Ik ben een VIP mijn naam is {self.name} - {self.customer_nr}'


# ------------------------------------------------

if __name__ == '__main__':

    p = Person('Peter', 'Lhee')

    print( p.tell() )

    p.move('Soesterberg')
    Person.move(p, 'Soesterberg')

    print( p.tell() )

    p2 = Person('Ger', 'Veendam')
    print( p2.tell() )

    customer = Customer('Arthur', 'Utrecht', 'BOL9842378923798')
    print(customer.tell())
