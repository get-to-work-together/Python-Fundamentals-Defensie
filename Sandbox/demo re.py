import re

while True:
    s = input('Geef een datum: ')

    if s == '':
        break

    regex = r'\d{1,2}-\d{1,2}-\d{4}|\d{4}-\d{1,2}-\d{1,2}'

    if re.match(regex, s):
        print('Dat is idd een datum')

    else:
        print('Dat is geen datum')