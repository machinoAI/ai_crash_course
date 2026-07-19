"""
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

What is lower bound?
The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

Example 1:
    Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
    Result: 1
    Explanation: Index 1 is the smallest index such that arr[1] >= x.

Example 2:
    Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
    Result: 3
    Explanation: Index 3 is the smallest index such that arr[3] >= x.
"""

# Brute force:
def lower_bound_finder(nums, x):
    for i, num in enumerate(nums):
        if num >= x:
            return i

    return len(nums)

nums = [3,5,8,15,19,21,27]
x = 21

print(lower_bound_finder(nums, x))


# Optimized: Best time and space complexity
def find_lower_bound(nums, x):
    low, high = 0, len(nums)-1
    ans =len(nums)
    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else:
           low = mid+1
    return ans

nums = [3,5,8,15,19]
x = 9

print(find_lower_bound(nums, x))

# Recursion: O(logn) & O(logn)
def lower_bound(nums, low, high, x):

    if low > high:
       return low

    mid = (low + high)//2

    if nums[mid] >= x:
        return lower_bound(nums, low, mid-1, x)

    return lower_bound(nums, mid+1, high, x)


def find_lower_bound(nums, x):
    return lower_bound(nums, 0, len(nums)-1, x)


nums = [1,2,2,3]
x = 2

nums = [3,5,8,15,19]
x = 9

print(find_lower_bound(nums, x))