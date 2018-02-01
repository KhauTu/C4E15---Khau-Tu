x = 10
while x:
    x = x - 1 # or x -= 1
    if x % 2 != 0: continue # Odd? --skip print
    print(x, end =' ')
    
y = 10
while y:
    y = y - 1 # or y -= 1
    if y % 2 == 0: # Odd? --skip print
        print(y, end =' ')
