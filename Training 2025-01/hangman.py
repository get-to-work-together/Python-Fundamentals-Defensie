import random

filename = '../Datasets/basiswoorden-gekeurd.txt'

with open(filename) as f:
    words = [word.strip() for word in f.readlines() if len(word.strip()) == 6]

secret_word = random.choice(words).upper()
# print(secret_word)

guessed_letters = set()
while True:
    print()
    print('Je hebt al de volgende letters ingevoerd:', ''.join(sorted(guessed_letters)))
    letter = input('Geef een letter: ')
    guessed_letters.add(letter.upper())

    all_letters_guessed = True
    response = ''
    for c in secret_word:
        if c in guessed_letters:
            response += f' {c} '
        else:
            response += ' _ '
            all_letters_guessed = False

    print(response)
    if all_letters_guessed:
        print('Yes! You guessed the word correctly.')
        break
