import random

# suits = ('clubs', 'diamonds', 'hearts', 'spades')
# or
# suits = 'clubs diamonds hearts spades'.split()
# or
suits = ('♣', '♢', '♡', '♠')

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()

cards = [f'{suit}{rank}' for rank in ranks for suit in suits]
# or
# cards = ['%s of %s' % (rank, suit) for rank in ranks for suit in suits]

random.shuffle(cards)

# hand = [cards.pop() for _ in range(5)]
# or
# hand = sorted(hand, key = lambda card: suits.index(card.split()[-1]))

# print(hand)

hands = []
for _ in range(4):
    hands.append( sorted([cards.pop() for _ in range(5)], key = lambda c: (suits.index(c[0]), ranks.index(c[1:]))) )
    # hands.append( sorted(cards.pop() for _ in range(5) ))

for i, hand in enumerate(hands, start = 1):
    print(f'Player {i}: {hand}')
