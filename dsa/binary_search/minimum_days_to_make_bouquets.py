"""
Minimum days to make M bouquets

Problem Statement: You are given 'N’ roses and you are also given an array 'arr' where 'arr[i]' denotes that the
'ith' rose will bloom on the 'arr[i]th' day. You can only pick already bloomed roses that are adjacent to make
a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses.
Return -1 if it is not possible.

Examples
Example 1:
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Example 2:
Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
Result: -1
Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

"""
def is_possible(bloom_days, day, m, k):
    count = 0
    bouquets = 0

    for bloom in bloom_days:
        if bloom <= day:
            count +=1

            if count == k:
                bouquets +=1
                count =0
        else:
            count =0

    return bouquets >= m

def min_days_to_make_bouquets(bloom_days, m, k):

    # m is bouquet counts
    # k number of roses required to make a bouquets
    # bloom days

    total_flower = m*k
    low = min(bloom_days)
    high = max(bloom_days)

    if total_flower > len(bloom_days):
        return -1

    for day in range(low, high+1):
        if is_possible(bloom_days, day, m, k):
            return day

    return  -1



bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3

bloom_days=[1, 10, 3, 10, 2]
m = 3
k=2
print(min_days_to_make_bouquets(bloom_days, m, k))






