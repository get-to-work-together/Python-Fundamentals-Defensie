import re

patroon = input('Geef patroon (gebruik . als wildcard karakter) : ')

regex = re.compile(r'\b' + patroon + r'\b')

print(regex.pattern)

filename = '../Datasets/basiswoorden-gekeurd.txt'
with open(filename) as f:
    woorden = [line.rstrip('\n') for line in f.readlines()]

print('Woorden die passen op jouw patroon:')
for woord in woorden:
    if regex.match(woord) and len(patroon) == len(woord):
        print(woord)
