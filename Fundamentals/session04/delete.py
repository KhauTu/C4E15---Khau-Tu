favs = ["death note", "netflix", "teaching"]

print("Hi there, here your favorite things so far")
# print(*favs, sep =", ") # pythonic

for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1, fav))

print("* " * 10)

x = int(input("Favorite position you want to get rid of?"))
favs.pop(x - 1)

for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1, fav))
