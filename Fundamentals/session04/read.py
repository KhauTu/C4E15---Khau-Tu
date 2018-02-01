favorite_things = ["death note", "netflix", "teaching"]

# print("Hi there, here your favorite things so far")
# print(*favorite_things, sep =", ") # pythonic

# more = input("Name one thing you want to add?")
# favorite_things.append(more)
#
# print(*favorite_things, sep =", ") # separator

for i in range(len(favorite_things)):
    print(i + 1,".", favorite_things[i])


favs = ["death note", "netflix", "teaching"]

# for fav in favs:
#     print(fav, end =", ")
# print()
print("* " * 10)

position = 1
#
# for fav in favs:
#     # print(fav, ". ", fav, sep = "")
#     print("{0}. {1}".format(position, fav))
#     position += 1

# for index, fav in enumerate(favs):
#     print(index + 1, ". ", fav, sep = "")
#     print("{0}. {1}".format(index + 1, fav))

# print(*enumerate(favs)) # not lazy-loading
