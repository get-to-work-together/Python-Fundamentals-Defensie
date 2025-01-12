filename = r'../Datasets/10-million-password-list-top-1000000.txt'

while True:

    password = input('Enter password to check: ')

    if password == '':
        break

    with open(filename, mode = 'r') as f:
        for line in f:
            line = line.rstrip()
            if password == line:
                print(f'Your password "{password}" is NOT safe. Please change!')
                break
        else:
            print(f'Your password "{password}" is safe.')




# with open(filename, mode = 'r') as f:
#     lines = set(line.rstrip() for line in f.readlines())
#
# if password in lines:
#     print('Your password is known. Please use an other password!')
# else:
#     print('Your password is safe.')