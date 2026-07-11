nums = [1, 1, 3, 3, 4, 4, 8, 8, 9]   # sorted array

from collections import  Counter


def lone_element(nums):
    list_freq = Counter(nums)   #O(n)

    print("list_freq:", list_freq)
    for k,v in list_freq.items():
        if v ==1:
            return k

print("Lone Element:",lone_element(nums))


def lone_element(nums):

    left = 0
    right = len(nums)-1

    while left < right:

       mid = (left + right) // 2

       if mid % 2 ==1:
           mid -=1

       if nums[mid] == nums[mid+1]:
            left = mid+2
       else:
            right = mid

    return nums[left]

def lone_element(nums):
    xorr = 0

    for num in nums:
        xorr ^=num

    return xorr


nums = [1, 1, 3, 3, 4, 4, 8, 8, 9]
print("Lone Element optimized:",lone_element(nums))
print("Lone Element XOR:",lone_element(nums))