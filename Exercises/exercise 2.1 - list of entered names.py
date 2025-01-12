
names = []
while True:
    name = input('Enter a name: ')

    if name:
        if name in names:
            print('Name is already in the list')
        else:
            names.append(name)
    else:
        break

print()
print('The names you entered were:')
for name in sorted(names):
    print(name)
