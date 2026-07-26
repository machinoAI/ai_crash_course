"""
Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

Example 1:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

Example 2:
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
Result: False
Explanation: The element 10 is not present in the array. So, the answer is False.

"""
def search_element_rotated_sorted_array_II(nums, target):

    low = 0
    high = len(nums)-1

    while low <= high:

        mid = (low+high)//2

        if nums[mid] == target:
            return  True

        if nums[low] == nums[mid] == nums[high]:
            low = low +1
            high = high-1

            continue

        if nums[low] <= nums[mid]:              #left half is sorted

            if nums[low] <= target <= nums[mid]: # if target lies in left half
                high = mid-1
            else:
                low = mid+1
        else:                                           # right half is sorted
            if nums[mid] <= target <= nums[high]:
               low = mid+1
            else:
                high = mid-1
    return False

nums = [4,5,6,7,0,1,2]
target = 3
print(search_element_rotated_sorted_array_II(nums, target))





