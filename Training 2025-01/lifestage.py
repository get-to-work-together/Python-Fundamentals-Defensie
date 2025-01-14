age = int(input('Wat is jouw leeftijd? '))

if age < 2:
    print('Baby')
elif age < 4:
    print('Toddler')
elif 4 <= age < 13:
    print('Kid')
elif 13 <= age < 20:
    print('Teenager')
elif 20 <= age < 65:
    print('Adult')
else:
    print('Elder')
