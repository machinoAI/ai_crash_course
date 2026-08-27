"""
Given a binary array containing only 0s and 1s, find the maximum length of a contiguous subarray with
    an equal number of 0s and 1s. Return both the length and the starting/ending indices.

Input: arr = [1, 0, 1, 1, 1, 0, 0]
Output: length = 6, indices = [1, 6]
"""

def longest_equal_subarray(nums):

    max_length = 0
    start = -1
    end = -1

    first_seen = {0:-1}
    balance = 0


    for i, num in enumerate(nums):

        if num == 0:
            balance -=1
        else:
            balance +=1


        if balance in first_seen:

            length = i - first_seen[balance]

            if length > max_length:

                max_length = length

                start = first_seen[balance] +1
                end = i

        else:
            first_seen[balance] = i

    return max_length, [start, end]


arr = [1, 0, 1, 1, 1, 0, 0]
print(longest_equal_subarray(arr))