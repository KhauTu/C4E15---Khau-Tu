nums = [7, 5, 10, 8, 200, 30]

num_to_find = int(input("Enter a number? "))

if num_to_find in nums: # 1 for loop
    print("Found")
    found_index = nums.index(num_to_find)
    print("Index:", found_index)
else:
    print("Not found")
