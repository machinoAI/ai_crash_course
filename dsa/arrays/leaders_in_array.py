"""
Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 The rightmost element (0) is always a leader.
7 and 1 are greater than the elements to their right, making them leaders as well.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader because there are no elements after it.
12 is greater than all the elements to its right (3, 0, 6), and 22 is greater than 12, 3, 0, 6, making them leaders as well.

"""

def array_leaders(nums):

    result = []

    for i in range(len(nums)):
        leader = True

        for j in range(i+1, len(nums)):
            if nums[j] >= nums[i]:
                leader = False
                break

        if leader:
            result.append(nums[i])

    return result




# nums = [4, 7, 1, 0]
nums = [10, 22, 12, 3, 0, 6]
print(array_leaders(nums))

# Optimized:
def array_leaders(nums):

    result = []

    if not nums:
        return result

    max_val = nums[-1]
    result.append(nums[-1])

    for i in range(len(nums)-2, -1, -1):
        if nums[i] > max_val:
            result.append(nums[i])
            max_val=nums[i]

    result.reverse()

    return result

nums = [10, 22, 12, 3, 0, 6]
print("Optimzed:", array_leaders(nums))