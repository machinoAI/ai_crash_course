"""
Floor and Ceil in Sorted Array:
You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x

Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

Example 2:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 8
Result: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.

"""
def ceil_floor(nums, x):
    ceil = -1
    floor = -1

    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == x:
            return nums[mid], nums[mid]

        elif nums[mid]> x:
            ceil = nums[mid]
            high = mid-1
        else:
            floor = nums[mid]
            low = mid+1
    return  floor, ceil

nums= [3, 4, 4, 7, 8, 10]
x = 5
x2 = 8
print(ceil_floor(nums, x))
print(ceil_floor(nums, x2))