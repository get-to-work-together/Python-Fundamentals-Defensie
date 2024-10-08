import random

required_length = random.randint(8, 12)

n_lowercase = 2
n_uppercase = 2
n_numbers = 1
n_special = 1

n_extra = max(0, required_length - n_lowercase - n_uppercase - n_numbers - n_special)

LOWERCASE_CHARACTERS = 'abcdefghijkmnopqrstuvwxyz'    # removed l
UPPERCASE_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'     # removed I and O
NUMBER_CHARACTERS = '0123456789'
SPECIAL_CHARACTERS = '@#$%&*+?!<>{}[]() _-'

EXTRA_CHARACTERS = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + NUMBER_CHARACTERS + SPECIAL_CHARACTERS

lower = random.choices(LOWERCASE_CHARACTERS, k = n_lowercase)
upper = random.choices(UPPERCASE_CHARACTERS, k = n_uppercase)
numbers = random.choices(NUMBER_CHARACTERS, k = n_numbers)
special = random.choices(SPECIAL_CHARACTERS, k = n_special)
extra = random.choices(EXTRA_CHARACTERS, k = n_extra)

all = lower + upper + numbers + special + extra

random.shuffle(all)

password = ''.join(all)

print(f'New password {password}')
