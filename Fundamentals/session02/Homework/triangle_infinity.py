x = int(input("how many level?"))
import random
from turtle import *
shape("arrow")
speed(0)
color("black", "red")
colors  = ["red","green","blue","orange","purple","cyan","magenta"]
penup()
def draw_triangle (sz):
    color(random.choice(colors))
    begin_fill()
    pendown()
    for i in range(3):
        forward(sz)
        left(120)
    end_fill()
    penup()
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line
def line(z, x):
    penup()
    setx(-350)
    sety(-300)
    forward(z*x-2*x)
    pendown()
    for i in pascal(z):
        if i%2==1:
            draw_triangle(x)
            seth(120)
            forward(x)
            seth(0)
        else:
            seth(120)
            forward(x)
            seth(0)
    seth(0)
for _1 in range(1, 2**x+1):
    line(_1, 6)

color("white", "white")
setx(-350)
sety(0)
mainloop()
