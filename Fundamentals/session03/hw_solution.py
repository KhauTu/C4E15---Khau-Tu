col = int(input("Enter column: "))
row = int(input("Enter row: "))
for y in range(row):
    for x in range(col):
        if (x + y) % 2 == 0:
            print("x", end="")
        else:
            print("*", end="")
    print()
