number = input('Geef een getal: ')

for digit in str(number):
    n = int(digit)
    print(n * '★')