from turtle import *

def draw_star(x, y, l):
    penup()
    goto(x, y)
    pendown()
    # setx(x)
    # sety(y)
    for i in range(5):
        right(144)
        forward(l)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()
