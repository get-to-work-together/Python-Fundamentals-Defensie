name = 'Guido'
age = 62

print(name + ' is ' + str(age) + ' years old')
print('%s is %d years old ' % (name, age))
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')

import math
print(f'pi = {math.pi:<10.3f}')
print(f'pi = {10*math.pi:^10.3f}')

print('pi = %.7f' % math.pi)

print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.startswith('A'))
print(name.startswith('G'))
print(name.lower().startswith('g'))
print(name.lower().endswith('o'))
print(name.lower().count('u'))
print('abacadabra'.lower().count('a'))
print(len(name))
print(name.lower().replace('d','t'))
print(name.find('d'))
print(name.index('d'))
print(name)
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
print(name[1:4])
print(name[1:])
print(name[:2])

