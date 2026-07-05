"""
Given an integer array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists in the array.


"""
# Brute Force (O(n²))
nums = [3,2,3]

def majority_element(nums):

    n = len(nums)

    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1

        if count>n//2:
            return nums[i]


print(majority_element(nums))

# Optimal Approach (Boyer-Moore Voting Algorithm) — O(n), O(1)

def majority_element(nums):
    count =0
    candidate = None

    for num in nums:
        if count==0:
            candidate=num

        if num == candidate:
            count +=1
        else:
            count -=1

    return candidate

nums = [3,2,3]
print(majority_element(nums))
