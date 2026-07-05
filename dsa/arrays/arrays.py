"""
An array stores elements contiguously in memory, allowing direct access using an index.

- Note: Python's list is a dynamic array, not a fixed-size array.
- nums = [10, 20, 30, 40]
- Arrays are chosen because they provide O(1) random access.
- Time complexity:

| Operation        | Complexity     |
| ---------------- | -------------- |
| Access           | O(1)           |
| Update           | O(1)           |
| Append           | Amortized O(1) |
| Search           | O(n)           |
| Insert Beginning | O(n)           | Every element shifts one position.
| Delete Beginning | O(n)           |
| Insert End       | Amortized O(1) |
| Delete End       | O(1)           |

# Read heavy application should use array as time complexity for reading is just: O(1)
# Write operation's is too expensive as time complexity O(n). Linked list should be a better idea.
#

Q1: Move all zeros to the end while preserving the order of non-zero elements.
Q2: Rotate an array to the right by k positions in-place.
Q3. Find the second largest element in one traversal without sorting.
Q4. Given an array, find the smallest missing positive integer in O(n) time and O(1) extra space.
Q5. Find the first duplicate element using O(1) extra space (when values are in the range 1 to n).

"""
