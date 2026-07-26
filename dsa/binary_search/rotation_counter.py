"""
Find out how many times the array has been rotated

Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.

Pre-requisites: Find minimum in Rotated Sorted Array,  Search in Rotated Sorted Array II & Binary Search algorithm

Examples
Input : arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

Input : arr = [3,4,5,1,2]
Output : 3
Explanation: The original array should be [1,2,3,4,5]. So, we can notice that the array has been rotated 3 times.
"""

def rotation_counter(nums):

    for i, num in enumerate(nums):
        if nums[i] >= nums[i+1]:
            return i+1

    return 0

nums = [4,5,6,7,0,1,2,3]
nums = [3,4,5,1,2]
nums = [8,1, 2, 3, 4,5]
print(rotation_counter(nums))


def rotation_counter(nums):
    low = 0
    high =len(nums)-1

    while low <= high:

        mid = low + (high-low)//2

        # if mid-element is greater than element at high
        # smallest lies to right of mid
        if nums[mid] >= nums[high]:
            low = mid+1
        else:
            # else smallest element is at mid or to the left.
            high= mid

    # when Low ==high, we find the smallest element
    return low