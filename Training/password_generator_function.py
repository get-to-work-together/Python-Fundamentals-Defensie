import random


def generate_password(required_length = 8,
                      n_lowercase = 1,
                      n_uppercase = 1,
                      n_numbers = 1,
                      n_special = 1):

    n_extra = max(0, required_length - n_lowercase - n_uppercase - n_numbers - n_special)

    lowercase_characters = 'abcdefghijkmnopqrstuvwxyz'  # removed l
    uppercase_characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # removed I and O
    number_characters = '0123456789'
    special_characters = '@#$%&*+?!'

    extra_characters = lowercase_characters + \
                       uppercase_characters + \
                       number_characters + \
                       special_characters

    lower = random.choices(lowercase_characters, k=n_lowercase)
    upper = random.choices(uppercase_characters, k=n_uppercase)
    numbers = random.choices(number_characters, k=n_numbers)
    special = random.choices(special_characters, k=n_special)
    extra = random.choices(extra_characters, k=n_extra)

    all = lower + upper + numbers + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password


# --------------------------------------------------------------------

if __name__ == '__main__':

    print(generate_password())

    print(generate_password(6, 0, 6, 0, 0))

    print(generate_password(6, n_numbers=6))