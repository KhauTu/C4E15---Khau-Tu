from random import *
from calc import *

def generate_quiz():
    x = randint(0, 10)
    y = randint(1, 10)
    error = randint(-1, 1)
    op_list = ["+"] * 3 + ["-"] * 2 + ["*"] + ["/"]
    op = choice(op_list)
    result = eval(x, y, op) + error
    # Hint: Return [x, y, op, result]
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    # print(x, y, op, result, user_choice)
    if (result == eval(x, y, op) and user_choice == True) or (result != eval(x, y, op) and user_choice == False):
        return True
        pass
    else:
        return False
        pass
