"""
There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Examples
Example 1:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation:
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

"""


def rearrange_array(nums, n):
    pos = []
    neg = []

    for i,num in enumerate(nums):
        if num>0:
            pos.append(num)
        else:
            neg.append(num)

    for i in range(n//2):
        nums[2*i] = pos[i]
        nums[2 * i+1] = neg[i]


    return nums

nums = [1,2,-4,-5]
print(rearrange_array(nums, 4))


