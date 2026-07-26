"""
Search Single Element in a sorted array

Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

Examples
Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Output: 4
Explanation: Only the number 4 appears once in the array.

Input: arr[] = {1,1,3,5,5}
Output : 3
Explanation: Only the number 3 appears once in the array.
"""

def search_single_element(nums):

    n = len(nums)

    if n==1:
        return nums[0]

    for i in range(n):

        if i == 0 :
            if nums[i] != nums[i + 1]:
                return nums[i]

        elif i == n-1:
            if nums[i] != nums[i-1]:
                return nums[i]

        else:
            if nums[i] != nums[i-1]  and nums[i] != nums[i+1]:
                return  nums[i]
    return -1

nums = [1,1,3,5,5]
nums = [1,1,2,2,3,3,4,5,5,6,6]
nums = [2,3,3,4,4]

print(search_single_element(nums))

def search_single_element(nums):

    ans = 0
    for i in range(len(nums)-1):
        ans ^= nums[i]

        return  ans

print(search_single_element(nums))



