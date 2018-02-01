numbers = [1, 6, 8, 1, 2, 1, 5, 6]

k = int(input("Enter a number? "))
# with count() function:
x = numbers.count(k)
print(k, "appears", x, "times in my list")

# without count() function:
num_count = 0
for i in numbers:
    if i == k:
        num_count += 1
print(k, "appears", num_count, "times in my list")
