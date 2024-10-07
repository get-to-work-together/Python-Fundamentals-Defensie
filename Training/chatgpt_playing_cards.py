import random

# Step 1: Define the 4 suits
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# Step 2: Define the 13 ranks
ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')

# Step 3: Combine the suits and ranks into a deck of cards
cards = [r + ' of ' + s for r in ranks for s in suits]

# Step 4: Shuffle the deck
random.shuffle(cards)

# Step 5: Draw 5 cards from the deck
hand = [cards.pop() for _ in range(5)]

# Step 6: Print the hand of cards
print("Your hand of cards is:")
for card in hand:
    print(card)
