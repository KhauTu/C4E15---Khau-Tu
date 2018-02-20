def eval(x, y, Op): # function argument

    R = 0 # R: Result

    if Op == "+":
        R = x + y
    elif Op == "-":
        R = x - y
    elif Op == "*":
        R = x * y
    elif Op == "/":
        R = x / y
    return R

# x = int(input("x = "))
# y = int(input("y = "))
# Op = input("Op = ")
#
# R = eval(x, y, Op)
#
# print("{0} {1} {2} = {3}".format(x, Op, y, R))

# x = int(input("x = "))
# Op = input("Operation(+,-,*,/): ")
# y = int(input("y = "))
# R = 0
#
# if Op == "+":
#     R = x + y
# elif Op == "-":
#     R = x - y
# elif Op == "*":
#     R = x * y
# elif Op == "-":
#     R = x / y
# else:
#     print("Unsupported operation")
# print("{0} {1} {2} = {3}".format(x, Op, y, R))
