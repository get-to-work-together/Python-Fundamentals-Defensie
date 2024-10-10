class TooLowException(Exception):
    pass


class TooHighException(Exception):
    pass


def foolproof_input(lower, upper):

    while True:

        try:

            user_input = input(f'Geef een getal tussen {lower} en {upper}: ')

            number = int(user_input)

            if number < lower:
                raise TooLowException('Getal is te laag')

            elif number > upper:
                raise TooHighException('Getal is te hoog')

            else:
                return number

        except ValueError:
            print(f'"{user_input}" is niet een getal.')

        except TooLowException as err:
            print(err)

        except TooHighException as err:
            print(err)

        except KeyboardInterrupt:
            print('Tot ziens')
            break


# ----------------------------------------------

getal = foolproof_input(1, 10)
if getal is not None:
    print(f'Je hebt het getal {getal} ingevoerd.')