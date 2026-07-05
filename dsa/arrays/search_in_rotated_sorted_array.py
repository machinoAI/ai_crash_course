"""
You are given a sorted array that has been rotated at some pivot.
Given the rotated array and a target value, return the index of the target.

If the target is not found, return -1.

You must solve it in O(log n) time.
"""

nums = [4,5,6,7,0,1,2]

target = 0
# nums =[2, 3, 4, 5, 3]


def rotated_array(nums, target):

    for i, num in enumerate(nums):
        if target == num:
            return i

    return -1


print(rotated_array(nums, target))


#Binary Search to achieve O(log n)

def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1