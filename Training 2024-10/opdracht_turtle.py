import turtle

# L
def draw_L():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)

# F
def draw_F():
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


def draw_star():
    n = 5
    angle = 180 - 36

    for _ in range(n):
        turtle.forward(200)
        turtle.right(angle)


def relocate(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.pensize(5)

draw_L()

# reposition
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(20)
turtle.pendown()

draw_F()

relocate(-200, -50)

turtle.color('red')

draw_star()

relocate(-400, 10)

draw_star()

turtle.hideturtle()
turtle.done()
