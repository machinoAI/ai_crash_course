"""
Given an integer array nums, return an array answer such that:

answer[i] is equal to the product of all the elements of nums except nums[i].
You must not use division.
The solution should run in O(n) time.

"""

nums = [1,2,3,4]

# output: [24,12,8,6]

#Method: Brute force:
def product_array(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i!=j:
                product *=nums[j]
        result.append(product)
    return result


print(product_array(nums))


#Method: Brute force: