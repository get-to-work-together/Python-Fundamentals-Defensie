
def banner(s, c = '*'):
    n = len(s)
    border = c * (n + 6)
    print(border)
    print(c + '  ' + s + '  ' + c)
    print(border)


user_input = input('Geef tekst: ')

banner(user_input)

banner(user_input, '$')
banner(user_input, c = '$')
