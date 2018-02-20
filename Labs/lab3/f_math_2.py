# list of operator +, -, *, / using choice()
from random import randint, choice
from calc import eval
while True:
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)
    R = 0
    Op_list = ["+"] * 3 + ["-"] * 2 + ["*"] + ["/"]
    Op = choice(Op_list)

    R = eval(x, y, Op) + error

    print("{0} {1} {2} = {3}".format(x, Op, y, R))

    Check = input("(Y/N?) ").upper()

    # Cach 1:
    if error == 0:
        if Check == "Y":
            print("Yay")
        else:
            print("Nay")
    else:
        if Check == "Y":
            print("Nay")
        else:
            print("Yay")
