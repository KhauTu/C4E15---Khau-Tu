# import numpy as np
# n = int(input("Enter a number? "))

# sequence = range(1, n+1)
# result = np.product(sequence) #pythonic

# print(result)

n = int(input("Product from 1 to n, with n = ")) + 1
factorial = 1 # initial condition

for i in range(1, n): # loop
    factorial *= i # factorial = factorial + i

print(factorial) # output
