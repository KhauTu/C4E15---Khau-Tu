from turtle import *

shape("turtle")
speed(10)
width(2)

def triangle():
    for i in range(3):
        forward(100)
        left(360 / 3)
def square():
   for i in range(4):
       forward(100)
       left(360 / 4)
def pentagon():
   for i in range(5):
       forward(100)
       left(360 / 5)
def hexagon():
   for i in range(6):
       forward(100)
       left(360 / 6)
color("blue")
triangle()
pentagon()

color("red")
square()
hexagon()

mainloop()
