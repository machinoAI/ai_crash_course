"""
Find the Smallest Divisor Given a Threshold

Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'.
Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the
 given array by it, the sum of the division's result is less than or equal to the given threshold value.

Examples
Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor.
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor.
Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively.
Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

Example 2:
Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
Result: 2
Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.

"""

def smallest_divisor(n, nums, limit):

    sum1 = 0
    for i in range(1, max(nums)+1):

        sum1 = sum((num+i-1)//i for num in nums)

        if sum1 <= limit:
            return i
    return -1

n = 5
nums = [1,2,3,4,5]
limit = 8
n = 4
nums = [8,4,2,3]
limit = 10

print(smallest_divisor(n, nums, limit))

import math
def smallest_divisor(n, nums, limit):

    low = 1
    high = max(nums)

    while low <= high:

        mid = (low+high)//2

        divisor_sum = sum((num+mid-1)//mid for num in nums)

        if divisor_sum <= limit:
            high = mid-1
        else:
            low = mid+1

    return low

print(smallest_divisor(n, nums, limit))
