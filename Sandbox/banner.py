
def banner(text):
    n = len(text)
    print('*' * (n + 6))
    print('*  ' + text    + '  *')
    print('*' * (n + 6))



def create_banner(text, c = '#'):
    n = len(text)
    s  = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(text, *args, **kwargs):
    print(create_banner(text, *args, **kwargs))


# ----------------------------------------------------------

if __name__ == '__main__':

    print_banner('Peter', '+')

























##
##
##
##
##
##def create_banner(text, c='#'):
##    n = len(text)
##    s  = c * (n + 6) + '\n'
##    s += c + '  ' + text + '  ' + c + '\n'
##    s += c * (n + 6)
##    return s
##
##def print_banner(text):
##    print(create_banner(text))
##
##
### ----------------------------------------------------------
##
##banner('Peter')
##
##print_banner('Peter')
