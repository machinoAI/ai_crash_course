"""
There are n stairs, and a person standing at the bottom wants to climb stairs to reach the top.
    The person can climb either 1 stair or 2 stairs at a time,
    the task is to count the number of ways that a person can reach at the top.

Input: n=4
Output: 5

"""

def climb_stairs(n):

    if n <= 2:
        return n

    two_back = 1   # ways to reach stair 0
    one_back = 2   # ways to reach stair 1

    for i in range(3, n + 1):
        current = one_back + two_back

        two_back = one_back
        one_back = current

    return one_back


print(climb_stairs(4))