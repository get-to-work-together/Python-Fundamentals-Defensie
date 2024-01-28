
def highest_even_odd(*numbers):
    highest_even = None
    highest_odd = None
    for number in numbers:
        if number % 2 == 0:
            if highest_even is None:
                highest_even = number
            elif number > highest_even:
                highest_even = number
        else:
            if highest_odd is None:
                highest_odd = number
            elif number > highest_odd:
                highest_odd = number
    return highest_even, highest_odd


# -------------------------------------------------------

print( highest_even_odd(4, 6, 7, 2, 4, 9, 7, 1) )
