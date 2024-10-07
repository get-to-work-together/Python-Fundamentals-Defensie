
def foolproof_input(lower, upper):

    while True:
        try:
            invoer = input(f'Geef een getal tussen {lower} en {upper}: ')

            if invoer.isdecimal():
                getal = int(invoer)

            else:
                print('Dat is geen getal.')
                continue

        except ValueError:
            print('Dat is een geheel getal. Voer een geheel getal in.')
            continue

        if lower <= getal <= upper:
            return getal
        else:
            print(f'Getal is niet tussen {lower} en {upper}')




getal = foolproof_input(1, 10)
print(f'Je hebt het getal {getal} ingevoerd.')