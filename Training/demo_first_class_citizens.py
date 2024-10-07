
s = 'dit is een beetje onzin met abacadabra en olediodiedio'

words = s.split()
print(words)


def aantal_klinkers(word):
    aantal = 0
    for letter in word:
        if letter in 'aeiou':
            aantal += 1
    return aantal


words.sort(key = lambda word: sum([word.count(klinker) for klinker in 'aeiou']))


for word in words:
    print(word)

