favorite_things = ["death note", "netflix", "teaching"]

print("Hi there, here your favorite things so far")
print(*favorite_things, sep =", ") # pythonic

more = input("Name one thing you want to add?")
favorite_things.append(more)

print(*favorite_things, sep =", ") # separator
