names = []

while True:
    name = input('Geef een naam: ')

    if name:
        names.append(name)
    else:
        break

for name in sorted(names):
    print(name)
