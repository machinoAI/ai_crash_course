
"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that
they add up to target.

nums = [2,7,11,15]
target = 9

Output:
[0,1]

"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return (i,j)


nums = [2,7,11,15]
target = 9
print("Two sum index: ",two_sum(nums,target))


# Optimized time complexity:

def two_sum_index(nums, target):

    seen = {}

    for i in range(len(nums)):


        temp = target-nums[i]

        if temp in seen:
            return seen[temp], i
        else:
            seen[nums[i]] = i

nums = [2,7,11,15]
target = 9
print("two_sum_index optimized: ", two_sum_index(nums, target))