"""
nums = [ 4, 5, 6, 5,4,3]

output = [6, 3 , 5, 5 , 4, 4]

"""

from collections import Counter

def sort_by_frequency(nums):
    freq = Counter(nums)

    return sorted(nums, key=lambda x: (freq[x], -x))


nums = [4, 5, 6, 5, 4, 3]

print(sort_by_frequency(nums))