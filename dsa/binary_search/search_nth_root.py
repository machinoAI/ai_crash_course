"""
Nth Root of a Number using Binary Search

Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

Examples
Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.
Input : N = 4, M = 69
Output: -1
Explanation : The 4th root of 69 does not exist. So, the answer is -1.

"""

def nth_root(n, m):

    for i in range(1, m):

        power = i**n

        if power == m:
            return  i
        if power > m:
            break

    return -1

n = 3
m =27
# n = 4
# m = 69
print(nth_root(n, m))

def nth_root(n, m):

    low = 1
    high = m

    while low <= high:

        mid =(low+high)//2

        if mid**n == m:
            return mid
        elif mid**n > m:
            high = mid -1
        else:
            low = mid+1
    return -1

print(nth_root(n, m))