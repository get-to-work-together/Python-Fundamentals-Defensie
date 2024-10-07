from datetime import date

class Person:

    def __init__(self, name, residence = None, geboortedatum = None):
        self.name = name
        self.residence = residence
        self.geboortedatum = geboortedatum

    def tell(self):
        leeftijd_text = f'Ik ben {self.leeftijd}.' if self.leeftijd else 'Leeftijd onbekend.'
        if self.residence is not None:
            return (f'I am {self.name} from {self.residence}. {leeftijd_text}')
        else:
            return (f'I am {self.name}. Ik ben dakloos. {leeftijd_text}')

    def move(self, new_residence):
        self.residence = new_residence

    @property
    def leeftijd(self):
        if self.geboortedatum is not None:
            return int((date.today() - date.fromisoformat(self.geboortedatum)).days // 365.25)
        else:
            return None

class Speler(Person):
    def __init__(self, name, residence, geboortedatum, rugnummer, positie):
        Person.__init__(self, name, residence, geboortedatum)
        self.rugnummer = rugnummer
        self.positie = positie

    def tell(self):
        return (f'I am {self.name} from {self.residence}. Ik ben {self.positie} en mijn rugnummer is {self.rugnummer}')




# ------------------------------------------------------------


p1 = Person('Peter')
print(p1.tell())



p1 = Person('Albert', 'Amsterdam')
print(p1.tell())
p1.move('Urk')
print(p1.tell())

p2 = Person('Gert Jan', 'Den Haag', '1999-02-25')
print(p2.tell())

p3 = Speler('Speler Gert Jan', 'Den Haag', '1958-02-28', 14, 'spits')
print(p3.tell())