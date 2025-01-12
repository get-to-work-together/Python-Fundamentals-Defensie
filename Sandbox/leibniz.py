
total = 1

erbij_tellen = False  # + or -
for i in range(3, 1000000000, 2):
    if erbij_tellen:
        total = total + 1 / i
    else:
        total = total - 1 / i
    erbij_tellen = not erbij_tellen

print('Pi is ongeveer: ', total * 4)

import math
print('Pi is : ', math.pi)
