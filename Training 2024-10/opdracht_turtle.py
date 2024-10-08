import turtle

turtle.pensize(5)

# L
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

# reposition
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(20)
turtle.pendown()

# F
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

# star
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.color('red')

n = 5
angle = 180 - 36

for _ in range(n):
    turtle.forward(200)
    turtle.right(angle)


turtle.hideturtle()
turtle.done()
