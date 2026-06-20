# Find unique (non-duplicate) elements in a list
#
# Input:  [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
# Output: [1, 4]   (elements that appear exactly once)

nums = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]

# Method 1: Using a for loop + count
new_list = []
for num in nums:
    if nums.count(num) == 1:
        new_list.append(num)

print("for loop:          ", new_list)

# Method 2: List comprehension (concise one-liner)
print("list comprehension:", [num for num in nums if nums.count(num) == 1])
