from random import randint, choice
from calc import eval

while True:
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)

    display_z = x + y + error
    print("{0} + {1} = {2}".format(x, y, display_z))
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
# Cach 2:
    # if (error == 0 and Check == "Y") or (error != 0 and Check == "N"):
    #     R = "Yay"
    # else:
    #     R = "You're wrong!"
    # print(R)
# Cach 3: Dung Boolean True False
