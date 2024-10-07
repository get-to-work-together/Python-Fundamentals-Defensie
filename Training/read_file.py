import os

while True:

    try:
        filename = input('Geef filename: ')

        if not os.path.exists(filename):
            print('file bestaat niet!')
            continue

        with open(filename, mode='r') as f:
            for line in f:
                line = line.strip()
                if 'regel' in line:
                    print(line)
        break

    except FileNotFoundError:
        print(f'File not found')
        print('Geef opnieuw.')

