"""
Finding Sqrt of a number using Binary Search

Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of sqrt(n).

Examples
Input: N = 36
Output: 6
Explanation: Square root of 36 is 6.
Input: N = 28
Output: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5.
"""


def find_square_root(num):


    for i in range(1, num):
        square = i*i

        if num == square:
            return i
        elif num < square:
            return i-1

num = 36
num = 28
num = 17
print(find_square_root(num))


