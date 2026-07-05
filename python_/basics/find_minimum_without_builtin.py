# Find the minimum number in a list without using the built-in min() function
#
# Input:  [10, 30, 90, 60, 40, 50]
# Output: 10
#
# Approach: Assume the first element is the min, then iterate and update
# whenever a smaller value is found.

nums = [10, 30, 90, 60, 40, 50]

min1 = nums[0]
for num in nums:
    if num < min1:
        min1 = num

print("Minimum:", min1)
# Output: Minimum: 10
