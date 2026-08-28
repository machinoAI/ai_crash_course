from collections import Counter

def sort_by_frequency(nums):
    freq = Counter(nums)

    return sorted(nums, key=lambda x: freq[x])


nums = [4, 5, 6, 5, 4, 3]

print(sort_by_frequency(nums))