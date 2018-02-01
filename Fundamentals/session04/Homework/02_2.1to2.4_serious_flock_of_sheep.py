# 2.1
sheep = [5, 7, 300, 90, 24, 50, 75]
print('''Hello, my name is Khau Tu and these are my ship sizes
{0}'''.format(sheep))
print()

# 2.2
print("Now my biggest sheep has size {0} let's shear it".format(max(sheep)))
print()

# 2.3
default_size = 8
k = sheep.index(max(sheep))
sheep[k] = default_size
print('''After shearing, here is my flock
{0}'''.format(sheep))
print()

# 2.4
for index, size in enumerate(sheep):
    sheep[index] = size + 50
print('''One month has passed, now here is my flock
{0}'''.format(sheep))
