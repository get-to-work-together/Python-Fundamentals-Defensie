

class Person:

    __slots__ = ['_name', '_residence']

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def __str__(self):
        return self._name + ' from ' + self._residence

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')


class Customer(Person):

    def __init__(self, name, residence, customer_number):
        super().__init__(name, residence)
        self._customer_number = customer_number

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}. I a customer {self._customer_number}.')


#=================================

if  __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')
    p1.tell()

    p2 = Person('Kazuko', 'Eindhoven')
    p2.tell()

    p3 = Customer('Patrick', 'Soesterberg', '12345')
    p3.tell()

    
