x = 0
y = 1
z = x + y
for i in range(5):
    if i == 0:
        x = x
        y = y
        z = z
    else:
        y = z
        z = x
        x = x + y

    m = x + z
    print("Month {0}: {1} pair(s) of rabbit".format(i, m))
