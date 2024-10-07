
names = []
while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)
    else:
        break

print()
print('The names you entered were:')
for name in sorted(names):
    print(name)
