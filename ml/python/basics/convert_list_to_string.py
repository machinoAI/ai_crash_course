# Convert a list of strings into a single string
#
# Input:  ["a", "b", "c", "d"]
# Output: "a b c d"
#
# Approach: str.join(iterable) concatenates all elements of the iterable,
# placing the separator string between each pair of elements.

list1 = ["a", "b", "c", "d"]

# Join with a space separator
mystring = " ".join(list1)
print("space-joined :", mystring)        # Output: a b c d

# Join with no separator (compact)
compact = "".join(list1)
print("no separator  :", compact)         # Output: abcd

# Join with a custom separator
csv = ",".join(list1)
print("comma-joined  :", csv)             # Output: a,b,c,d
