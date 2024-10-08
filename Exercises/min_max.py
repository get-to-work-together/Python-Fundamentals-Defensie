"""
min_max function

Written by Peter Anema

History:
First version 15 september 2021
"""

import random


def min_max(*numbers):
    """Calculate the minimum and maximum number of the arguments in one pass"""
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum


def min_max_sorted(*numbers):
    """Calculate the minimum and maximum number of the arguments by using the sorted function"""
    sorted_numbers = sorted(numbers)
    minimum = sorted_numbers[0]
    maximum = sorted_numbers[-1]
    return minimum, maximum


# --------------------------------

if __name__ == '__main__':

    import random
    numbers = [random.randint(1, 10000) for _ in range(10)]

    print(numbers)

    minimum, maximum = min_max(*numbers)

    print('Minimum:', minimum)
    print('Maximum:', maximum)
