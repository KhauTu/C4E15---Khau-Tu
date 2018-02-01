from random import randint
# 1
result = randint (1, 100)
print(result)
Loop = True

# 2
while Loop:
    guess = int(input("Your number in range [1, 100]: "))

# 3
    if guess < result:
        print("it is too small!")
    elif guess > result:
        print("it is too large!")
    else:
        print("Bingo")
        Loop = False
