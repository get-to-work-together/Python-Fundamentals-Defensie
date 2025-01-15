filename = '../Datasets/10-million-password-list-top-1000000.txt'

password = input('Welk wachtwoord wil je controleren? : ')
with open(filename) as f:
    for line in f:
        line = line.strip()
        if password in line:
            print('Dat wachtwoord is bekend. Verander je wachtwoord!')
            break
    else:
        print('Wachtwoord is OK!')







#
#
# with open(filename) as f:
#     known_passwords = [password.strip() for password in f.readlines()]
#
# while True:
#     password = input('Welk wachtwoord wil je controleren? : ')
#
#     if password == '':
#         break
#
#     if password in known_passwords:
#         print('Dat wachtwoord is bekend. Verander je wachtwoord!')
#     else:
#         print('Jouw wachtwoord kom niet voor in de lijst.')
