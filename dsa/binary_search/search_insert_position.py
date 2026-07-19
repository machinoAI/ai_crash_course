"""
You are given a sorted array arr of distinct values and a target value x.
 You need to search for the index of the target value in the array.

Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.
"""

#Brute force:

def search_insert_position(nums, x):

    for i, num in enumerate(nums):

        if num >= x:
            return i

    return len(nums)
nums = [1, 2, 4, 7]
x = 6
x2 = 2

print(search_insert_position(nums, x))
print(search_insert_position(nums, x2))

# Optimized:

def search_insert_position(nums, x):
    low = 0
    high = len(nums)-1
    ans = len(nums)

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans

print(search_insert_position(nums, x))
print(search_insert_position(nums, x2))