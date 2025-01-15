import string
import random

min_length = 12
max_length = 18

password_length = random.randint(min_length, max_length)

n_upper = 3
n_lower = 3
n_digits = 1
n_special = 1
n_extra = password_length - n_upper - n_lower - n_digits - n_special

upper = random.choices('ABCDEFGHJKLMNPQRSTUWVXYZ', k=n_upper)   # remove O en I
lower = random.choices('abcdefghijklmnopqrstuwvxyz', k=n_lower)  # remove l
digits = random.choices('0123456789', k=n_digits)
special = random.choices('!@#$%^&*()_+-=<>?/|.,', k=n_special)
extra = random.choices('ABCDEFGHJKLMNPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz', k=n_extra)

all_characers = upper + lower + digits + special + extra

random.shuffle(all_characers)

password = ''.join(all_characers)

print(password)


count_upper = 0
count_lower = 0
count_digits = 0
count_special = 0

for c in password:
    if c in string.ascii_uppercase:
        count_upper += 1
    elif c in string.ascii_lowercase:
        count_lower += 1
    elif c in string.digits:
        count_digits += 1
    elif c in string.punctuation:
        count_special += 1

password_ok = all([count_upper > 0,
                   count_lower > 0,
                   count_digits > 0,
                   count_special > 0])

if password_ok:
    print('Password is OK')
else:
    print('Password is NOT OK!')
