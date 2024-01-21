
def banner(text):
    n = len(text)
    print((n + 6) * '*')
    print('*  ' + text + '  *')
    print((n + 6) * '*')


# ------------------------------------------------------------------

name = input('Wat is jouw naam? : ')

banner(name)
