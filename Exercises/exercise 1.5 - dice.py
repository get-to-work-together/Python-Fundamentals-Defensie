import random

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
# dice3 = random.randint(1, 6)
# dice4 = random.randint(1, 6)
# dice5 = random.randint(1, 6)
#
# total = dice1 + dice2 + dice3 + dice4 + dice5
#
# print('Thrown', dice1, dice2, dice3, dice4, dice5)
# print('Total', total)



# n = 5
# total = 0
# for i in range(n):
#     dice = random.randint(1, 6)
#     print('Thrown', dice)
#     total += dice
#
# print('Total', total)





#   DRY - Don't Repeat Yourself








die = []
for _ in range(20):
    die.append(random.randint(1, 6))

print('Thrown', die)
print('Total', sum(die))




# die = [random.randint(1, 6) for _ in range(5)]
#
# print('Thrown', die)
# print('Total', sum(die))





# dice = []
# for _ in range(5):
#     dice.append( random.randint(1, 6) )
#
# print('Thrown', dice)
# print('Total', sum(dice))


# dice = [random.randint(1, 6) for _ in range(5)]
#
# print('Thrown', dice)
# print('Total', sum(dice))
