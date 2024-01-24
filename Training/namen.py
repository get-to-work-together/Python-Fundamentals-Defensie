names = []
while True:

    name = input('Geef een naam: ')

    if name == '':
        break

    names.append(name)


print(f'Er zijn {len(names)} namen ingevoerd.')
print('Entered names:')
for name in sorted(names):
    print(name)