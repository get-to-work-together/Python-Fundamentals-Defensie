gender = 'm'

match gender:
    case 'm':
        print('Sir')
    case 'v'|'f':
        print('Madame')
    case _:
        print('Person')