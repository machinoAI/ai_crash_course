"""
Search Element in a Rotated Sorted Array


22

Problem Statement: Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.

Examples
Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output :4
Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output :-1
Explanation :Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.
"""


def search(nums, target):

    low = 0
    high = len(nums)-1

    while low <= high:

        mid = (low+high)//2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:  # if left side is sorted
            if nums[low] <= target < nums[mid]:  # target is left side
                high = mid-1
            else:
                low = mid+1

        else:
            if nums[mid] < target <= nums[high]:  # target is left side
                low = mid + 1
            else:
                high = mid - 1
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target  = 0
print(search(nums, target))