filename = '10-million-password-list-top-1000000.txt'

password = input('Give a password to check: ')

with open(filename) as f:
    known_passwords = f.readlines()