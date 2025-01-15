import math

def print_goodmorning(name, n=1):
    for _ in range(n):
        print(f'Goodmorning {name}.')
    print('How are you today?')
    print('Have a great day!')


def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius



# -------------------------------------------------

x = input('Geef een naam: ')
print_goodmorning(x)

print_goodmorning('Peter', n=2)
print_goodmorning('Marc', n=3)

r = float(input('Geef straal van een cirkel: '))
opp = circle_area(r)
print(f'Oppervlakte: {opp}')
print(f'Omtrek: {circle_circumference(r)}')
