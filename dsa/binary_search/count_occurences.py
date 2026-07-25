"""
You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

Example 1:
Input:
 N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output
: 4
Explanation:
 3 is occurring 4 times in
the given array so it is our answer.

Example 2:
Input:
 N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output
: 5
Explanation:
 2 is occurring 5 times in the given array so it is our answer.

"""

n = 7
nums = [2, 2 , 3 , 3 , 3 , 3 , 3,4]
target = 3

def first_occurrence(n, nums, target):
    low = 0
    high = n-1
    first = -1

    while low <= high:

        mid = (low+high)//2

        if nums[mid] == target:
            first = mid
            high = mid-1
        elif  nums[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return first



def last_occurrence(n, nums, target):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            last = mid
            low = mid + 1

        elif nums[mid] < target:
            low = mid+1

        else:
            high = mid - 1

    return last

def first_last_occurrences(n, nums, target):
    first = first_occurrence(n, nums, target)

    if first == -1:
        return -1, -1

    last =  last_occurrence(n, nums, target)

    return first, last

def count_occurrences(n, nums, target):

    first, last = first_last_occurrences(n, nums, target)

    if first == -1:
        return 0
    else:
        return (last - first+1)


print(count_occurrences(n, nums, target))




