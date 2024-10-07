import re

patroon = input('Geef patroon (gebruik . als wildcard karakter) : ')
regex = re.compile('^' + patroon + '$')

print('Woorden die passen op jouw patroon:')

filename = 'basiswoorden-gekeurd.txt'
with open(filename) as f:
    for line in f:
        line = line.strip()
        if regex.match(line):
            print(line)
