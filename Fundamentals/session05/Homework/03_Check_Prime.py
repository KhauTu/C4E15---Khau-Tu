# def primes_lessthan(n):
#     result = []
#     for i in range(2,n):
#         if is_prime(i):
#             result.append(i)

y = int(input("Enter your number: "))
x = y // 2

while x > 1:
    if y % x == 0:
        print(y, 'is not a Prime number')
        break
    x -= 1
else:
    print (y, "is a Prime number")
