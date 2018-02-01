from turtle import *

shape("turtle")
speed(10)

color("red" , "yellow")
width(2)

for i in range(4):
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(120)
    forward(50)
    left(60)
    forward(50)
    right(30)

mainloop()
