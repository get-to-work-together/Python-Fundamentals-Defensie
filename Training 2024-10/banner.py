def create_banner(text, c = '*', upper=False):
    if upper:
        text = text.upper()
    n = len(text)
    top_line = (n + 6) * c
    banner = top_line + '\n' + f'{c}  {text}  {c}' + '\n' + top_line
    return banner


def print_banner(text, c = '*', upper=False):
    print(create_banner(text, c, upper))


# ----------------------------------------------------------------

if __name__ == '__main__':

    naam = input('Geef naam: ')

    print_banner(naam)
    print_banner(naam, '$', upper=True)

