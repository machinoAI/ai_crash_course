# Q5. Find the first duplicate element using O(1) extra space (when values are in the range 1 to n).

"""
Input:
[1, 9, 3, 2, 4,8, 7, 3,7]

Output:
2

"""


def duplicate(nums):

   for num in nums:
       index = abs(num)-1
       if nums[index]<0:
           return  abs(num)
       nums[index] *= -1


nums = [1, 2,3,7,4,5,7,6]
print(duplicate(nums))