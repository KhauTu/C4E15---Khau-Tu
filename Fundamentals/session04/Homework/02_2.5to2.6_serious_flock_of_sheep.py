sheep = [5, 7, 300, 90, 24, 50, 75]
print('''Hello, my name is Khau Tu and these are my ship sizes
{0}'''.format(sheep))
print()

print("Now my biggest sheep has size {0} let's shear it".format(max(sheep)))

default_size = 8
k = sheep.index(max(sheep))
sheep[k] = default_size
print('''After shearing, here is my flock
{0}'''.format(sheep))
print()

# 2.5
month = 3
for i in range(month):
    print("MONTH {0}".format(i+1))
    # 1
    for index, size in enumerate(sheep):
        sheep[index] = size + 50
    print('''One month has passed, now here is my flock
    {0}'''.format(sheep))
    # 2
        # 2.6
    sum = 0
    for index, size in enumerate(sheep):
        total_size = sum + size
        sum = total_size

    if total_size <= 1000:
        print("Now my biggest sheep has size {0} let's shear it".format(max(sheep)))
        # 3
        default_size = 8
        k = sheep.index(max(sheep))
        sheep[k] = default_size
        print('''After shearing, here is my flock
        {0}'''.format(sheep))
    else:
        price = 2
        money = price * total_size
        print("My flock has size in total: {0}".format(total_size))
        print("I would get {0} * {1}$ = {2}$".format(total_size, price, money))
#
# # 2.6
# sum = 0
# for index, size in enumerate(sheep):
#     total_size = sum + size
#     sum = total_size
# price = 2
# money = price * total_size
# print("My flock has size in total: {0}".format(total_size))
# print("I would get {0} * {1}$ = {2}$".format(total_size, price, money))
