
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(3, 3)
v2 = Vector(2, -2)

print(v1)
print(v2)

v3 = v1 + v2

print(v3)