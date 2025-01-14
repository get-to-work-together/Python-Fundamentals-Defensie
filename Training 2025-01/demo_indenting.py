age = 15
gender = 'v'

if gender == 'm':
    print('de heer')

elif gender == 'v':
        print('mevrouw')

else:
    print('beste x')


print('Hoe gaat het?')



import random


total = 0
counter = 0
while counter < 5:
    print(counter)
    dice = random.randint(1, 6)
    total += dice
    print(dice)
    counter += 1
print(f'Total: {total}')

total = 0
for _ in range(5):
    dice = random.randint(1, 6)
    total += dice
    print(dice)
print(f'Total: {total}')


for item in ['appels', 'peren', 'bananen']:
    print(item.upper())

magic_number = 13
for i in range(1, 21):
    if i == magic_number:
        continue
    print(i)


