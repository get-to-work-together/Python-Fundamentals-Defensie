import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

counter = 0
while True:
    guess = int(input('What is your (next) guess? '))
    counter += 1
    if guess > secret_number:
        print('lower ...')
    elif guess < secret_number:
        print('higher ...')
    else:
        print(f'YEAAAH!!!! You guessed it in {counter} guesses. The number was {secret_number}. ')
        break
