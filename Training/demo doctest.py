
def cube(x):
    """Calculate the cube of x

    >>> cube(10)
    1000

    >>> cube(2)
    8
    """

    return x ** (2 + 1)


# -----------

if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)

    print(help(cube))