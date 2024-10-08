import math
import random

low = 1
high = 100

number_of_guesses = 0
while True:
    next_guess = (low + high) // 2

    response = input('Is your number %d? : ' % next_guess).lower().strip()
    number_of_guesses += 1

    if response.startswith('h'):    # e.g. higher
        low = next_guess + 1

    elif response.startswith('l'):  # e.g. lower
        high = next_guess

    elif response.startswith('y'):  # e.g. yes
        print("YEAH! Guessed it in %d guesses" % number_of_guesses)
        break

    else:
        print('Invalid answer! Valid answer are "[h]igher", "[l]ower" or "[y]es."')
        number_of_guesses -= 1

    if low >= high:
        print("You cheated! I quit.")
        break
