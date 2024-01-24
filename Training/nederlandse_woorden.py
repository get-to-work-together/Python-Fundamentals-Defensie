filename = 'basiswoorden-gekeurd.txt'

f = open(filename)
woorden = [line.rstrip('\n') for line in f.readlines()]
f.close()

while True:
    user_input = input('Geef een woord: ')

    if user_input == '':
        break

    if user_input.lower() in woorden:
        print('Dat is inderdaad een bekend nederlands woord.')

    else:
        print('Dat is NIET een bekend nederlands woord.')