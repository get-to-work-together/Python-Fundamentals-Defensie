import unittest


def doet_iets(a, b, c):
    """

    >>> doet_iets(4, 5, 6)
    61

    >>> doet_iets(0, 0, 0)
    0

    >>> doet_iets(1, 1, 1)
    14

    """
    result = 10 * a + 3 * b + c
    return result



class MyTests(unittest.TestCase):

    def test1(self):
        expected = 61
        actual = doet_iets(4, 5, 6)
        self.assertEquals(expected, actual)

    def test2(self):
        expected = 0
        actual = doet_iets(0, 0, 0)
        self.assertEquals(expected, actual)

    def test3(self):
        expected = 15
        actual = doet_iets(1, 1, 1)
        self.assertEquals(expected, actual)




if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)

    unittest.main()