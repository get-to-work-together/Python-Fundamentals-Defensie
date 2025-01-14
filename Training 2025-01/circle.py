import math

radius = float(input('Geef straal: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Straal', radius)
print('Oppervlakte', area)
print('Omtrek', circumference)

print()

print('Straal ' + str(radius))
print('Oppervlakte ' + str(area))
print('Omtrek ' +  str(circumference))

print()

print(f'Straal {radius:.2f}')
print(f'Oppervlakte {area:.2f}')
print(f'Omtrek {circumference:.2f}')

