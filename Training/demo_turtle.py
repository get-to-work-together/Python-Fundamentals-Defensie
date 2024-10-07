from turtle import *

# -----------------------------------------
# Variabelen

stap_grootte = 100
hoek = 108
aantal_stappen = 16
color = 'orange'
turtle_speed = 5

# -----------------------------------------
# Algoritme

speed(turtle_speed)

fillcolor(color)

# begin_fill()
#
# for i in range(aantal_stappen):
#     forward(stap_grootte)
#     left(hoek)
#
# end_fill()

letter_size = 20
w = 5 * letter_size
h = 11 * letter_size
d = 2 * letter_size

# Draw L
# begin_fill()
#
# forward(w)
# left(90)
# forward(d)
# left(90)
# forward(w - d)
# right(90)
# forward(h - d)
# left(90)
# forward(d)
# left(90)
# forward(h)
#
# end_fill()

# Draw F

half_height = h / 2

begin_fill()

forward(d)
left(90)
forward(half_height)
right(90)
forward(w * 0.9 - d)
left(90)
forward(d)
left(90)
forward(w * 0.9 - d)
right(90)
forward(half_height - 2 * d)
right(90)
forward(w - d)
left(90)
forward(d)
left(90)
forward(w)
left(90)
forward(h)



end_fill()


exitonclick()
