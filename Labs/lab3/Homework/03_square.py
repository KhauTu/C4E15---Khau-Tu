from turtle import *

shape("turtle")
speed(10)
width(2)

def draw_square(l, c):
    color(c)
    for i in range(4):
        forward(l)
        left(360 / 4)
    # mainloop()
# l = int(input("length = "))
# c = input("color = ")
# square(l, c)
draw_square(100, "blue")

mainloop()
