import turtle as t


def draw_uppercase_l(size = 20, color = 'black'):

    t.color(color)

    w = 5 * size
    h = 9 * size
    d = 1 * size

    t.begin_fill()

    t.forward(w)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(w - d)
    t.right(90)
    t.forward(h - d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(h)
    t.left(90)

    t.end_fill()

    t.up()
    t.forward(w)
    t.down()


def draw_uppercase_f(size = 20, color = 'black'):

    t.color(color)

    w = 5 * size
    h = 9 * size
    d = 1 * size

    half_height = h / 2

    t.begin_fill()

    t.forward(d)
    t.left(90)
    t.forward(half_height)
    t.right(90)
    t.forward(w * 0.9 - d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(w * 0.9 - d)
    t.right(90)
    t.forward(half_height - 2 * d)
    t.right(90)
    t.forward(w - d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)

    t.end_fill()

    t.up()
    t.forward(w)
    t.down()


def draw_letter(letter):
    if letter == 'L':
        draw_uppercase_l()
    elif letter == 'F':
        draw_uppercase_f()

def inter(size = 10):
    t.up()
    t.forward(size)
    t.down()

def draw_text(text):
    for c in text:
        draw_letter(c)
        inter()

# ---------------------------------------

if __name__ == '__main__':

    t.speed(15)

    size = 10

    draw_text('LLL')

    t.hideturtle()
    t.exitonclick()
