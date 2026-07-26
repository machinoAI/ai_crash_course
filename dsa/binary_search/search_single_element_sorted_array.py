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
from collections import Counter

def search_single_element(nums):

    for k,v in Counter(nums).items():
        if v == 1:
            return k
    return -1


nums = [1, 1, 3, 5, 5]
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# nums = [2,3,3,4,4]

print("Brute Force: ", search_single_element(nums))

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

print("Brute Force-1: ", search_single_element(nums))

def search_single_element(nums):
    n = len(nums)
    ans = 0
    for i in range(n):
        ans ^= nums[i]

    return  ans

print("Brute Force-II: ",search_single_element(nums))


def search_single_element(nums):

    low = 1
    n = len(nums)
    high =n-1

    if n==1:
        return  nums[0]

    if nums[0] != nums[1]:
        return nums[0]

    if nums[high] != nums[high-1]:
        return nums[high]

    while low <= high:
        mid = (low+high)//2

        if nums[mid] !=nums[mid-1] and nums[mid] !=nums[mid+1]:
            return nums[mid]

        # If mid is in the left half (pairing is valid)
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            low = mid + 1
        else:
            high = mid - 1


    return -1


print("Optimised: ",search_single_element(nums))
