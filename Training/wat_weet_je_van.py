import json
import difflib
import random

f = open('vragen.json')
vragen = json.load(f)
f.close()

maximaal_aantal_antwoorden = 10

while True:

    vraag = random.choice(vragen)

    antwoorden = [v.lower() for v in vraag['A']]

    print(vraag['Q'])

    gegeven_antwoorden = set()
    goede_antwoorden = set()
    totaal_aantal_punten = 0
    while True:
        if len(gegeven_antwoorden) > maximaal_aantal_antwoorden:
            print('Je bent af!')
            break

        user_input = input('> ').lower()

        if user_input in gegeven_antwoorden:
            continue

        gegeven_antwoorden.add(user_input)

        for antwoord in antwoorden:
            matching_answers = difflib.get_close_matches(user_input, [antwoord], n=1, cutoff=0.6)
            if matching_answers:
                break
        else:
            matching_answers = None

        if matching_answers:
            punten = (10, 20, 30, 40)[len(goede_antwoorden)]
            print(f'YES! {punten} punten erbij.')
            totaal_aantal_punten += punten
            goede_antwoorden.add(matching_answers[0])

            if len(goede_antwoorden) == 4:
                print('Alles goed.')
                break

        else:
            continue

    print(f'Je hebt {totaal_aantal_punten} punten verzameld.')

    nog_een_keer = input('Wil je nog een vraag? [ja/nee] ')
    if nog_een_keer.lower() != 'ja':
        break
