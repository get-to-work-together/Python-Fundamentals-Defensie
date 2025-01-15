import string
import random


def generate_password(password_length: int = None,
                      n_upper: int = 3,
                      n_lower: int = 3,
                      n_digits: int = 1,
                      n_special: int = 1):

    """Generate a random password according to the specifications"""

    min_length = 8
    max_length = 18
    if password_length is None:
        password_length = random.randint(min_length, max_length)

    n_extra = max(0, password_length - n_upper - n_lower - n_digits - n_special)

    upper = random.choices('ABCDEFGHJKLMNPQRSTUWVXYZ', k=n_upper)   # remove O en I
    lower = random.choices('abcdefghijklmnopqrstuwvxyz', k=n_lower)  # remove l
    digits = random.choices('0123456789', k=n_digits)
    special = random.choices('!@#$%^&*()_+-=<>?/|.,', k=n_special)
    extra = random.choices('ABCDEFGHJKLMNPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz', k=n_extra)

    all_characers = upper + lower + digits + special + extra

    random.shuffle(all_characers)

    password = ''.join(all_characers)

    return password


def check_password(password: str,
                   min_length: int = 8,
                   min_upper: int = 1,
                   min_lower: int = 1,
                   min_digits: int = 1,
                   min_special: int = 1):

    count_upper = 0
    count_lower = 0
    count_digits = 0
    count_special = 0

    length = len(password)

    for c in password:
        if c in string.ascii_uppercase:
            count_upper += 1
        elif c in string.ascii_lowercase:
            count_lower += 1
        elif c in string.digits:
            count_digits += 1
        elif c in string.punctuation:
            count_special += 1

    password_ok = all([length >= min_length,
                       count_upper >= min_upper,
                       count_lower >= min_lower,
                       count_digits >= min_digits,
                       count_special >= min_special])

    return password_ok


# ----------------------------------------------------------------

print('>>', __name__)

if __name__ == '__main__':

    password = generate_password(8, 8, 0, 0, 0)

    print(password)

    if check_password(password):
        print('Password is OK')
    else:
        print('Password is NOT OK!')
