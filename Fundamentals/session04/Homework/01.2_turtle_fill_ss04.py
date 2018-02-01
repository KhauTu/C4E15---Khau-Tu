from turtle import *

shape("arrow")
speed(0)
width(2)

colors = ["red", "blue", "brown", "yellow", "grey"]

for index, line in enumerate(colors):
    color(line)
    begin_fill()
    for i in range(index+1):
        for i in range(2):
            right(90)
            forward(100)
            right(90)
            forward(50 * (5 - index))
    end_fill()

mainloop()
