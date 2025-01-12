import turtle

class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Vector(%d, %d)' % (self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5 

class Path:

    def __init__(self):
        self._vectors = []

    def add(self, vector):
        self._vectors.append(vector)

    def __repr__(self):
        return '\n'.join(map(str, self._vectors))

    def draw(self, factor = 30):
        for v in self._vectors:
            x, y = turtle.pos()
            turtle.goto(x + v._x * factor, y + v._y * factor)
        
        


#=====================================================


v1 = Vector(3, 3)
v2 = Vector(-2, 3)

p = Path()
p.add(v1)
p.add(v2)
p.add(v1)
p.add(Vector(3, -7))
p.add(Vector(-5, -2))

print(p)

p.draw()
turtle.done()






