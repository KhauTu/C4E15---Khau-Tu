from turtle import *

shape("turtle")
speed(10)

length = 10

for i in range(80):
    forward(i)
    length += 5
    left(90)

mainloop()
