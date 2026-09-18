"""
Input :  [4,4,4,4,2,2,2,2,4,4,4,4]

Output: [4,2,4]
"""


def remove_duplicate(nums):

    result = []


    for num in nums:

        if not result or result[-1] !=num:

            result.append(num)


    return result


nums = [4,4,4,4,2,2,2,2,4,4,4,4]
print(remove_duplicate(nums))