number = int(input("Enter a number:"))
Loop = True

x = 0
while Loop:
    bound = 10 ** x
    if (number - bound) < 0:
        print("digits: ", x)
        Loop = False
    else:
        x += 1

from math import log

digits = 0

while n > 0:
    digits += 1
    # remove the last digits
    n = n // 10

print(digits)
