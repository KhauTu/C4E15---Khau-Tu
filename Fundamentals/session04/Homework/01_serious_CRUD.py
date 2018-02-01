clothes = ["T-Shirt", "Sweater"]
choice = ["C", "R", "U", "D"]
Loop = True
while Loop:
    CRUD = input("Welcome to our shop, what do you want {0}? ".format(choice))
    if CRUD == "C":
        new = input("Enter new item: ")
        clothes.append(new)
    elif CRUD == "R":
        pass
    elif CRUD == "U":
        new_po = int(input("Update position? "))
        new = input("New item? ")
        clothes[new_po - 1] = new
    elif CRUD == "D":
        del_po = int(input("Delete position? "))
        clothes.pop(del_po - 1)
    else:
        print("please only choose in {0}".format(choice))
        break
    print("Our items:", end =" ")
    print(*clothes, sep =", ")
# else:
#     print()
