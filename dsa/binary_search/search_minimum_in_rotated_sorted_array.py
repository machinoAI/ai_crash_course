"""
Minimum in Rotated Sorted Array

Problem Statement:
Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is rotated at any index which is unknown. Find the minimum element in the array.

Input: arr = [4,5,6,7,0,1,2,3]
Output: 0
Explanation: The minimum element in the array is 0.

Input : arr = [3,4,5,1,2]
Output: 1
Explanation : The minimum element in the array is 1.
"""


def find_minimum_rotated_sorted_array(nums):
    low = 0
    high = len(nums)-1

    min_value = float("inf")

    while low <= high:

        mid = (low+high)//2

        if nums[low] <= nums[mid]:
            min_value = min(min_value, nums[low])
            low = mid+1
        else:
            high = mid-1

    return min_value



nums = [4,5,6,7,0,1,2,3]
nums= [3,4,5,1,2]
print(find_minimum_rotated_sorted_array(nums))