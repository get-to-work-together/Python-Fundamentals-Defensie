import re

filename = '../Datasets/basiswoorden-gekeurd.txt'

with open(filename) as f:
    woorden = [word.strip() for word in f.readlines()]

regex = input('Geef een regular expression: ')
regex = '^' + regex + '$'

for woord in woorden:
    if re.search(regex, woord):
        print(woord)
