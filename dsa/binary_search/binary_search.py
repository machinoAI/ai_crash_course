"""
You are given a sorted array of integers and a target, your task is to search for the target in the given array.
 Assume the given array does not contain any duplicate numbers.
conditions:
    - Sorted Array
    - No duplicates
    -

"""

def binary_search(nums, target):

    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            low = mid+1
        else:
           high = mid-1

    return -1

# print(binary_search(nums, 4))


nums = [3,4,6,7,9,12,16]
target = 12

print(binary_search(nums, target))

# Recursion:

def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high)//2

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, mid+1, high, target)
    else:
        return binary_search(arr, low, mid-1, target)

def search(nums, target):
    return binary_search(nums, 0, len(nums)-1, target)



nums = [3,4,6,7,9,12,16]
target = 4
print(search(nums, target))
