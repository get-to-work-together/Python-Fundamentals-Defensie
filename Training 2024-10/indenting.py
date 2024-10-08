

gender = 'm'


if gender == 'm':
    print('Geachte heer ...')

elif gender == 'v':
    print('Geachte mevrouw ...')

else:
    print('Geachte individu ...')

print('Hoe gaat het?')


for i in [4, 6, 8, 7, 1]:
    print(i)

for item in ['A', 'Beee', 'CCCC', 342]:
    print(item)

for c in 'abcdefg':
    print(c)

magic_number = 13
for i in range(1, 21):
    if i == magic_number:
        continue
    print(i)