"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
that has the largest product, and return that product.

"""

nums = [2,3,-2,4]
nums = [-2,3,-4]
#output : 6

def max_product_subarray(nums):

    current_max = nums[0]
    current_min = nums[0]
    result = nums[0]

    for num in nums[1:]:
        if num <0 :
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result =max(result, current_max)

    return  result


print(max_product_subarray(nums))