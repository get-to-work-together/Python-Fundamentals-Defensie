
try:

    user_input = input('Geef een getal: ')

    getal = int(user_input)

    print(getal)

except ValueError as ex:

    print('FOUT!', ex)