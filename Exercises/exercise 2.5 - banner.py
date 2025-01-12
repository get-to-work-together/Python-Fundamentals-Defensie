
def banner(name, c = None):
    if c is None:
        c = '*'
    n = len(name)
    print((n + 6) * c)
    print(c + '  ' + name + '  ' + c)
    print((n + 6) * c)


# ------------------------------------------------------------------

name = input('Wat is jouw naam? : ')
symbol = input('Welke symbool? : ') or None

banner(name, symbol)
