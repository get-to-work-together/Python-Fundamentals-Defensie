filename = '1000000-most-common-passwords.txt'

# f = open(filename)
# wachtwoorden = f.readlines()
# f.close()
# print(wachtwoorden[:10])

f = open(filename)
wachtwoorden = [line.rstrip('\n') for line in f.readlines()]
f.close()

# n = 10
# print(f'De eerste {n} wachtwoorden:')
# for wachtwoord in wachtwoorden[:n]:
#     print(wachtwoord)

while True:
    user_input = input('Geef een wachtwoord: ')

    if user_input == '':
        break

    if user_input in wachtwoorden:
        print('Dat wachtwoord is een bekende wachtwoord. Dus NIET gebruiken!')

    else:
        print('Dat is een onbekende wachtwoord. Hou het voor jezelf.')