def banner(s, c='*'):
    n = len(s)
    print((n + 6) * c)
    print(f'{c}  {s}  {c}')
    print((n + 6) * c)


def box_banner(s):
    n = len(s)
    print('┏' + (n+4) * '━' + '┓')
    print('┃  ' + s + '  ┃')
    print('┗' + (n+4) * '━' + '┛')


# ---------------------------------------

banner('Peter')
banner('ABRACADABRA')
banner('ABRACADABRA', '#')
banner('ABRACADABRA', c='$')
box_banner('Peter')