import random

class Game:

    def __init__(self, *players):
        self._players = players
        self._active_player_index = 0
        self.dice = Dice()

    def play(self):
        end_of_game = False
        round = 0
        while not end_of_game:
            round += 1

            print('-' * 80)
            active_player = self._players[self._active_player_index]
            print(f'{active_player.name}, jij bent aan de beurt.')

            active_player.turn()

            if round > 10:
                end_of_game = True

            self._active_player_index = game.next_player_index

    @property
    def next_player_index(self):
        number_of_players = len(self._players)
        return (self._active_player_index + 1) % number_of_players



class Player:

    def __init__(self, name):
        self._name = name
        self._card = Card()

    @property
    def name(self):
        return self._name

    @property
    def card(self):
        return self._card

    def turn(self):
        dice = Dice()
        print(dice)

        print(self.card)
        self.card.mark('g5')
        self.card.mark('r3')
        self.card.mark('x')

        print(self.card)


class Dice:

    def __init__(self):
        self.throw()
        self._combinations = self.combinations()

    def throw(self):
        self._red = random.randint(1, 6)
        self._yellow = random.randint(1, 6)
        self._green = random.randint(1, 6)
        self._blue = random.randint(1, 6)
        self._white1 = random.randint(1, 6)
        self._white2 = random.randint(1, 6)

    def combinations(self):
        return {
            'w1w2': self._white1 + self._white2,
            'w1r': self._white1 + self._red,
            'w2r': self._white2 + self._red,
            'w1y': self._white1 + self._yellow,
            'w2y': self._white2 + self._yellow,
            'w1g': self._white1 + self._green,
            'w2g': self._white2 + self._green,
            'w1b': self._white1 + self._blue,
            'w2b': self._white2 + self._blue,
        }

    def __str__(self):
        return f'Gegooid: wit {self._white1} - wit {self._white2} - rood {self._red} - geel {self._yellow} - groen {self._green} - blauw {self._blue}'

class Card:

    def __init__(self):
        self._red = []
        self._yellow = []
        self._green = []
        self._blue = []
        self._forfeit = 0
        self._total_red = 0
        self._total_yellow = 0
        self._total_green = 0
        self._total_blue = 0
        self._total_forfeit = 0
        self._score = 0

    def mark(self, cell):
        """
        Mark of a cell on a Qwixx card
        :param card: The card to use
        :param cell: The cell to mark off. E.g. 'b2', 'r8'
        :return: None
        """
        print('Marking cell ' + cell)

        color = cell[0]

        if color == 'x':
            self._forfeit += 1
            return True

        number = int(cell[1:])

        if number < 2 or number > 12:
            print('Alleen getallen tussen 2 en 12 zijn toegestaan.')
            return False

        d = {'r': {'numbers': self._red, 'direction': 'up'},
             'y': {'numbers': self._yellow, 'direction': 'up'},
             'g': {'numbers': self._green, 'direction': 'down'},
             'b': {'numbers': self._blue, 'direction': 'down'}}

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

    def score(self):
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

        self._total_red = points[len(self._red)]
        self._total_yellow = points[len(self._yellow)]
        self._total_green = points[len(self._green)]
        self._total_blue = points[len(self._blue)]
        self._total_forfeit = self._forfeit * 5

        self_score = self._total_red + \
                     self._total_yellow + \
                     self._total_green + \
                     self._total_blue - \
                     self._total_forfeit

    def __str__(self):
        def color_row(color, direction = 'up', marked = None):
            s = f'{color:8}'
            if direction == 'up':
                start = 2
                step = 1
                last = 12
                stop = last + 1
            elif direction == 'down':
                start = 12
                step = -1
                last = 2
                stop = last -1
            for number in range(start, stop, step):
                s += f'{number:6}' + \
                     ('X' if marked is not None and number in marked else ' ')
            return s

        s  = 'Kaart:\n'
        s += color_row('Rood', direction = 'up', marked = self._red) + '\n'
        s += color_row('Geel', direction = 'up', marked = self._yellow) + '\n'
        s += color_row('Groen', direction = 'down', marked = self._green) + '\n'
        s += color_row('Blauw', direction = 'down', marked = self._blue) + '\n'
        s += 'Mislukte worpen ' + self._forfeit * ' X'
        return s


#---------------------------------------------------------------------

if __name__ == '__main__':

    player1 = Player('Peter')
    player2 = Player('André')

    game = Game(player1, player2)

    game.play()