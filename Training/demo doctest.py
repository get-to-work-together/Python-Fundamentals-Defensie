import unittest

def square(n):
    """Calculate the square of n.

    >>> square(9)
    81

    >>> [square(n) for n in range(6)]
    [0, 1, 4, 9, 16, 25]
    """
    return n ** 2


class TestFunction(unittest.TestCase):

    def test1(self):
        result = square(9)
        expected = 81
        self.assertEquals(result, expected)

    def test2(self):
        result = square(-9)
        expected = 81
        self.assertEquals(result, expected)



if __name__ == "__main__":
    unittest.main()