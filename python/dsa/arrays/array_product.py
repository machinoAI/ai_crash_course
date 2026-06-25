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


# print(product_array(nums))


#Method: Optimized: O(n) time complexity:
nums = [1,2,3,4]

def product_array(nums):
    product =1
    product1=1
    left =[]
    right =[]
    index =0

    for num in nums:
        left.append(product)
        product *= num

    for num in reversed(nums):
        right.append(product1)
        product1 *=num



    rev_right=right[::-1]
    return [l * r for l, r in zip(left, rev_right)]


print(product_array(nums))