filename = '10-million-password-list-top-1000000.txt'

password = input('Give a password to check: ')

with open(filename) as f:
    for line in f:
        line = line.rstrip('\n')
        if line == password:
            print(f'Your password "{password}" is known. Change your password!')
            break
    else:
        print('Your password is OK.')

