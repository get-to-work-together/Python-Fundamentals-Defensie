from turtle import *

unit = 20

speed(10)
fillcolor('blue')

# begin_fill()
# forward(200)
# left(90)
# forward(100)
# left(90)
# forward(200)
# left(90)
# forward(100)
# end_fill()
# done()

# # L
# begin_fill()
# forward(5 * unit)
# left(90)
# forward(1 * unit)
# left(90)
# forward(4 * unit)
# right(90)
# forward(8 * unit)
# left(90)
# forward(1 * unit)
# left(90)
# forward(9 * unit)
# left(90)
# end_fill()

# # move for next
# penup()
# goto(200, 0)
# pendown()

# F
def draw_F(unit):
    begin_fill()
    forward(1 * unit)
    left(90)
    forward(4 * unit)
    right(90)
    forward(3 * unit)
    left(90)
    forward(1 * unit)
    left(90)
    forward(3 * unit)
    right(90)
    forward(3 * unit)
    right(90)
    forward(4 * unit)
    left(90)
    forward(1 * unit)
    left(90)
    forward(5 * unit)
    left(90)
    forward(9 * unit)
    end_fill()

draw_F(10)

penup()
forward(3 * unit)
pendown()

draw_F(8)
draw_F(6)
draw_F(5)


# path = '5L1L4R8L1L9'    # L
# path = '1L4R3L1L3R3R4L1L5L9'    # F

# begin_fill()
# for c in path:
#     if c == 'L':
#         left(90)
#     elif c == 'R':
#         right(90)
#     else:
#         d = int(c)
#         forward(d * unit)
# end_fill()

# n = 21
# angle = 180 - (n - 2) * 180 / n
# begin_fill()
# for _ in range(n):
#     forward(3 * unit)
#     left(angle)
# end_fill()

hideturtle()
done()
