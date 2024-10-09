import string

s = r'''\
Soesterberg is een dorp in het noordoosten van de Nederlandse provincie Utrecht gelegen tussen de plaatsen Amersfoort, Zeist en Soest. Het maakt deel uit van de gemeente Soest. Op 1 januari 2023 telde het dorp 7.535 inwoners. Soesterberg ligt tussen de provinciale weg Amersfoort-Utrecht (N237) en de autosnelweg A28.'''

s = s.lower().translate(str.maketrans('', '', string.punctuation + ''))

words = s.split()

unique_words = set(words)

d = {}
for word in sorted(unique_words):
    d[word] = words.count(word)

for word, n in d.items():
    print(f'{word:25}: {n:3}')