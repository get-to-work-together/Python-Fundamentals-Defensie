
names = []
while True:
    name = input('Enter a name: ')

    if name == '':
        break

    names.append(name)


print()
print('The names you entered were:')
for name in sorted(names):
    print(name)
