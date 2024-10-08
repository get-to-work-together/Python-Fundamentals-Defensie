
import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:

    if number_of_guesses == 0:
        prompt = 'What is your guess? '
    else:
        prompt = 'What is your next guess? '

    guess = int(input(prompt))

    number_of_guesses += 1

    if guess > secret_number:
        print('lower ...')

    elif guess < secret_number:
        print('higher ...')

    else:
        print(f'YEAAAH!!!! The number was {secret_number}. You guessed it in {number_of_guesses} guesses.')
        break
