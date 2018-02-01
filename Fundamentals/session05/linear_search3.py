nums = [5, 7, 10, 300, 20]

num_to_find = int(input("Enter a number? "))

for index, num in enumerate(nums):
    if num == num_to_find:
        print("Found at index:", index)
        break
else:
    print("Not found")
