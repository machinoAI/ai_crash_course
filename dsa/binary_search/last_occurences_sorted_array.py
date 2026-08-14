"""
Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key.
If the target is not found then return -1. Note: Consider 0 based indexing


"""
nums = [3, 4, 13, 13, 13, 20, 40]
target = 13

def last_occurrence(nums, target):

    low = 0
    high = len(nums)-1
    result = -1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            low = mid + 1
            result = mid
        elif  nums[mid] < target:
            low = mid+1
        else:
            high=mid-1
    return result


print(last_occurrence(nums, target))


