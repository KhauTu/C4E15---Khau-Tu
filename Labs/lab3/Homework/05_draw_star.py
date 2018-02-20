from turtle import *

shape("turtle")
speed(10)
width(2)

def draw_star(x, y, l):
    penup()
    goto(x, y)
    pendown()
    # setx(x)
    # sety(y)
    for i in range(5):
        right(144)
        forward(l)
    # mainloop()
# x = int(input("x = "))
# y = int(input("y = "))
# l = int(input(" length = "))
# draw_star(x, y, l)

draw_star(50, 50, 200)

mainloop()
