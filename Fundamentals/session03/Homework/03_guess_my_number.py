from random import randint
from getpass import getpass
print('Guess your number game')
x = int(getpass('Now think of a number from 0 to 100, then press Enter', ))

print('All you have to do is to answer my guess')
print('c if my guess is Correct')
print('s if my guess is Smaller than your number')
print('l if my guess is Larger than your number')

max_num = 101
min_num = 1
Guess = randint(1, 101)

while Guess != x:
    QA = print("Is", Guess, "your number?", end ='')
    if Guess > x:
        input()
        max_num = Guess
        Guess = (max_num + min_num) // 2
    elif Guess < x:
        input()
        min_num = Guess
        Guess = (max_num + min_num) // 2
else:
    QA = print("Is", Guess, "your number?", end ='')
    print('c')
print('I knew it')

# # 1
# result = randint (1, 100)
# print(result)
# Loop = True
#
# # 2
# while Loop:
#     guess = int(input("Your number in range [1, 100]: "))
#
# # 3
#     if guess < result:
#         print("it is too small!")
#     elif guess > result:
#         print("it is too large!")
#     else:
#         print("Bingo")
#         Loop = False
