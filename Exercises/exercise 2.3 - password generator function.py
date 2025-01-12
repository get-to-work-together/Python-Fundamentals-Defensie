import random
import string


def generate_password(required_length = None,
                      n_lowercase = 1,
                      n_uppercase = 1,
                      n_numbers = 1,
                      n_special = 1,
                      invalid_chars = 'l IO \\ \' \"'):

    if required_length is None:
        required_length = random.randint(8, 20)

    lowercase_characters = [c for c in string.ascii_lowercase if c not in invalid_chars]    # remove l
    uppercase_characters = [c for c in string.ascii_uppercase if c not in invalid_chars]     # remove I and O
    number_characters = [c for c in string.digits if c not in invalid_chars]
    special_characters = [c for c in string.punctuation if c not in invalid_chars]

    lower = random.choices(lowercase_characters, k = n_lowercase)
    upper = random.choices(uppercase_characters, k = n_uppercase)
    numbers = random.choices(number_characters, k = n_numbers)
    special = random.choices(special_characters, k = n_special)
    extra = random.choices(lowercase_characters +
                           uppercase_characters +
                           number_characters +
                           special_characters,
                           k = max(0, required_length - n_lowercase - n_uppercase - n_numbers - n_special))

    all_characters = lower + upper + numbers + special + extra

    random.shuffle(all_characters)

    password = ''.join(all_characters)

    return password


def check_password(password,
                   required_length = 8,
                   required_n_lowercase = 2,
                   required_n_uppercase = 2,
                   required_n_digits = 1,
                   required_n_special = 1):

    n_uppercase = 0
    n_lowercase = 0
    n_digits = 0
    n_special = 0
    for c in password:
        if c in string.ascii_uppercase:
            n_uppercase += 1
        elif c in string.ascii_lowercase:
            n_lowercase += 1
        elif c in string.digits:
            n_digits += 1
        elif c in string.punctuation:
            n_special += 1

    if len(password) < required_length:
        return False
    elif n_lowercase < required_n_lowercase:
        return False
    elif n_uppercase < required_n_uppercase:
        return False
    elif n_digits < required_n_digits:
        return False
    elif n_special < required_n_special:
        return False
    else:
        return True


def wachtwoord_met_invoer():
    required_length = int(input('Hoe lang? '))
    n_lowercase = int(input('Aantal kleine letters? '))
    n_uppercase = int(input('Aantal hoofdletters? '))
    n_numbers = int(input('Aantal cijfers? '))
    n_special = int(input('Aantal speciale karakters? '))

    wachtwoord = generate_password(required_length,
                                   n_lowercase,
                                   n_uppercase,
                                   n_numbers,
                                   n_special)

    return wachtwoord


# -----------------------------------------------------

print('New password: ', generate_password())
print('New password: ', generate_password(required_length = 7))
print('New password: ', generate_password(20))

print('New password: ', generate_password(required_length = 7, n_uppercase = 5))

# print(wachtwoord_met_invoer())

# wachtwoord = input('Geef wachtwoord: ')
# if check_password(wachtwoord):
#     print('Wachtwoord is OK.')
# else:
#     print('Wachtwoord voldoet niet aan de eisen.')
