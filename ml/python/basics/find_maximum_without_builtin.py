# Find the maximum number in a list without using the built-in max() function
#
# Input:  [10, 30, 90, 60, 40, 50]
# Output: 90
#
# Approach: Assume the first element is the max, then iterate and update
# whenever a larger value is found.

nums = [10, 30, 90, 60, 40, 50]

max1 = nums[0]
for num in nums:
    if num > max1:
        max1 = num

print("Maximum:", max1)
# Output: Maximum: 90
