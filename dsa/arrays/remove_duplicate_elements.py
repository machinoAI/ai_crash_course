"""
Remove Duplicates in-place from Sorted Array:
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
Input:[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]

"""
nums = [1,1,2,2,2,3,3]

def remove_duplicate_elements(nums):
    unique_nums = set()

    if not nums:
        return 0

    for num in nums:
        if num not in unique_nums:
            unique_nums.add(num)

    return list(unique_nums)

print(remove_duplicate_elements(nums))


#optimized solution:

def remove_duplicate_elements(nums):
    if not nums:
        return 0

    i =0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i+1     #nums[:i+1]

print("optimized:", remove_duplicate_elements(nums))