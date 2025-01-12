
class InvalidArgumentException(Exception):
    pass


def get_number(lower = 0, upper = 10):
    while True:
        try:
            number = int(input('Geef een getal: '))

            if number < lower or number > upper:
                raise InvalidArgumentException('invalid argument')

            return number

        except ValueError:
            print('Dat is niet een getal!')

        except InvalidArgumentException as ex:
            print(ex)
            print('Dat is niet een getal tussen 1 en 10!')



# -------------

print( 'Het getal is', get_number(1, 10) )