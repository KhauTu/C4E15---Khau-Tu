nums = [7, 5, 10, 8, 200, 30]

num_to_find = int(input("Enter a number?"))

# 1. Assumption / Gia dinh ve ket qua
found_index = -1 # Not found
# found_indexes = []

# 2. Creat a loop to test our Assumption
for index, num in enumerate(nums):
    if num == num_to_find:
        found_index = index # Update assumption
        print("Found")
        break

# 3. Print results
if found_index == -1:
    print("Not found")
else:
    print("Found at index", found_index)
    # else:
    #     print("Not found")
