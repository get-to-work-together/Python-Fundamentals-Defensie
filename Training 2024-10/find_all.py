
def find_all(s, to_find):
    return [i for i, c in enumerate(s) if c == to_find]


def find_all(s, to_find):
    p = -1
    return [p := s.find(to_find, p + 1) for _ in range(s.count(to_find))]


# ---------------------------------------------------

print( find_all('abcdabba', 'a') )
