
while True:
    try:
        getal = int(input('Geef een getal: '))

        result1 = 1e3 * getal

        result2 = 1 / getal

        if getal < 0:
            raise Exception('Negatief getal.')

        print('Duizend keer dat getal is: ', result1)

        print('Het omgekeerd van het getal is: ', result2)

    except ValueError:
        print('Dat is niet een getal!!!!!')
        continue

    except ZeroDivisionError:
        print('Kan niet door 0 delen!!!!')
        continue

    except Exception as ex:
        print('Er ging iets mis!!!!!', ex)
        continue

    else:
        break

    finally:
        print('Done')


