"""
Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

What is Upper Bound?
The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

The upper bound is the smallest index, ind, where arr[ind] > x.

Examples
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.

Example 2:
Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
Result: 4
Explanation: Index 4 is the smallest index such that arr[4] > x.

"""
# Brute force:O(n) & O(1)

def upper_bound_finder(nums, x):

    for i, num in enumerate(nums):
        if num > x:
            return i

    return len(nums)


nums = [3,5,8,9,15,19]
x = 9
print(upper_bound_finder(nums, x))


# Optimised force:O(log n) & O(1)

def upper_bound_finder(nums, x):

    low = 0
    high = len(nums)-1
    ans = len(nums)

    while low <=high:

        mid = (low+high)//2

        if nums[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

nums = [3,5,8,9,15,19,20]
x = 19
print(upper_bound_finder(nums, x))