"""
Sort the given list
nums = [8,3,55,33,1,99,833,0,-1]
output=[-1,0,1,3,8,33,55,99,833]
"""

def sort_numbers(nums):

    n = len(nums)

    for i in range(n):
        for j in range(n-1):

            if nums[j] > nums[j+1]:

                nums[j+1], nums[j] = nums[j], nums[j+1]

    return nums

nums = [-8,3,55,33,1,99,833,0,-1]
print(sort_numbers(nums))
