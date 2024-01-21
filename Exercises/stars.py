number = input('Geef een getal: ')

for c in number:
    print(c, f'{ord(c):3}', ord(c) * '*')