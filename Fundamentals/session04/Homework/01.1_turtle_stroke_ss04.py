from turtle import *

shape("arrow")
speed(10)
width(2)

colors = ["red", "blue", "brown", "yellow", "grey"]

for index, line in enumerate(colors):
    color(line)
    for i in range(index + 3):
        forward(100)
        left(360 / (index + 3))

mainloop()
