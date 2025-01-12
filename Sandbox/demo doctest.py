def square(n):
    """Calculate the square of n.

    >>> square(5)
    25
    >>> [square(n) for n in range(6)]
    [0, 1, 4, 9, 16, 25]
    """

    return n ** 2

print(square(13))