# zip() — Combine Multiple Iterables Element-by-Element
#
# zip(*iterables) pairs up elements from each iterable at the same index,
# producing tuples. It stops at the shortest iterable.
#
# Input:
#   a = [1, 2, 3]
#   b = [4, 5, 6]
#   c = [7, 8, 9]
# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

merged = zip(a, b, c)
print(list(merged))
# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# zip with unequal lengths — stops at the shortest
x = [1, 2, 3, 4]
y = [10, 20]
print(list(zip(x, y)))
# Output: [(1, 10), (2, 20)]

# Unzipping — use zip(*zipped) to reverse
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
print("nums   :", nums)     # Output: (1, 2, 3)
print("letters:", letters)  # Output: ('a', 'b', 'c')
