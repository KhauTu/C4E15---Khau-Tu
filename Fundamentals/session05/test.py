# person = ["Tuan Anh", 22, 2, "Ha Noi", "Moc Chau", 5, 4, "Maria", "Ping pong"]

# person = {}
# print(person)
#
# person = {
#     # key : value
#     "name": "Tuan Anh"
# }
# print(person)

person = {
    "name": "Tuan Anh",
    "age": 22,
    "sex": "male"
}

# print(person)
# if "age" in person:
#     print( person["age"] )

# Iterate by key
# for key in person:
#     print(key, person[key])

# Iterate by value
# for value in person.values():
#     print(value)

for key, value in person.items():
    print(key, value)
print(person.items())

person["age"] += 1
print(person)

# Công thức create và update giống nhau
person["projects"] = 5
print(person)

del person["sex"]
print(person)
