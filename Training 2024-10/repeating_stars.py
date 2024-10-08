number = input('Geef een getal: ')

for digit in number:
    line = '★' * int(digit)
    print(line)
