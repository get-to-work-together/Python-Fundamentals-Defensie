import random

empty_card = {
    'player': '',
    'red': [],
    'yellow': [],
    'green': [],
    'blue': [],
    'forfeit': 0,
    'total_red': 0,
    'total_yellow': 0,
    'total_green': 0,
    'total_blue': 0,
    'total_forfeit': 0,
    'score': 0
}


def mark(card, cell):
    """
    Mark of a cell on a Qwixx card
    :param card: The card to use
    :param cell: The cell to mark off. E.g. 'b2', 'r8'
    :return: None
    """
    print('Marking cell ' + cell)

    color = cell[0]

    if color == 'x':
        card['forfeit'] += 1
        return True

    number = int(cell[1:])

    if number < 2 or number > 12:
        print('Alleen getallen tussen 2 en 12 zijn toegestaan.')
        return False

    d = {'r': {'numbers': card['red'], 'direction': 'up'},
         'y': {'numbers': card['yellow'], 'direction': 'up'},
         'g': {'numbers': card['green'], 'direction': 'down'},
         'b': {'numbers': card['blue'], 'direction': 'down'}}

    numbers = d[color]['numbers']
    direction = d[color]['direction']

    valid = True
    if direction == 'up':
        if number > max([1] + numbers):
            numbers.append(number)
        else:
            print(f'Can only mark numbers higher than {max(numbers)}')
            return False

    elif direction == 'down':
        if number < min([13] + numbers):
            numbers.append(number)
        else:
            print(f'Can only mark numbers lower than {min(numbers)}')
            return False

    return True


def score(card):
    points = {
        0: 0,
        1: 1,
        2: 3,
        3: 6,
        4: 10,
        5: 15,
        6: 21,
        7: 28,
        8: 36,
        9: 45,
        10: 55,
        11: 66,
        12: 78
    }

    card['total_red'] = points[len(card['red'])]
    card['total_yellow'] = points[len(card['yellow'])]
    card['total_green'] = points[len(card['green'])]
    card['total_blue'] = points[len(card['blue'])]
    card['total_forfeit'] = card['forfeit'] * 5

    card['score'] = card['total_red'] + \
                    card['total_yellow'] + \
                    card['total_green'] + \
                    card['total_blue'] - \
                    card['total_forfeit']


def throw_quixx_dice():
    """"
    >>> len(throw_quixx_dice())
    6
    """
    d = {
        'red': random.randint(1, 6),
        'yellow': random.randint(1, 6),
        'green': random.randint(1, 6),
        'blue': random.randint(1, 6),
        'white1': random.randint(1, 6),
        'white2': random.randint(1, 6)
    }
    return d


def combinaties(throw):
    combis = [
    ]





# ------------------------------------------------------------------------

card1 = empty_card.copy()
card1['player'] = 'Peter'

print(card1)

mark(card1, 'r9')
print(card1)

mark(card1, 'r2')
print(card1)

mark(card1, 'g11')
print(card1)

mark(card1, 'g11')
print(card1)

mark(card1, 'g10')
print(card1)

mark(card1, 'g8')
print(card1)

mark(card1, 'g5')
print(card1)

mark(card1, 'x')
print(card1)

score(card1)
print(card1)
