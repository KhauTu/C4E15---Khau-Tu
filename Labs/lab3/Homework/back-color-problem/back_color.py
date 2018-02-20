from random import *
from is_inside_11 import *
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
text_list = []
color_list = []
rect_list = []
for i in range(len(shapes)):
    shapes_dict = shapes[i]
    text_list.append(shapes_dict['text'])
    color_list.append(shapes_dict['color'])
    rect_list.append(shapes_dict['rect'])

def get_shapes():
    return shapes

def generate_quiz():
    text = choice(text_list)
    color = choice(color_list)
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if text.upper() == 'BLUE' and is_inside([x, y], rect_list[0]) == True:
            return True
        elif text.upper() == 'RED' and is_inside([x, y], rect_list[1]) == True:
            return True
        elif text.upper() == 'YELLOW' and is_inside([x, y], rect_list[2]) == True:
            return True
        elif text.upper() == 'GREEN' and is_inside([x, y], rect_list[3]) == True:
            return True
        else:
            return False
    if quiz_type == 1:
        if color == '#3F51B5' and is_inside([x, y], rect_list[0]) == True:
            return True
        elif color == '#C62828' and is_inside([x, y], rect_list[1]) == True:
            return True
        elif color == '#FFD600' and is_inside([x, y], rect_list[2]) == True:
            return True
        elif color == '#4CAF50' and is_inside([x, y], rect_list[3]) == True:
            return True
        else:
            return False
