from turtle import *

shape("turtle")
speed(10)
width(2)

def draw_square(l, c): # l = length, c = color
    color(c)
    for i in range(4):
        forward(l)
        left(360 / 4)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
