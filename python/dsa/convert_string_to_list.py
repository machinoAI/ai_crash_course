# Convert a string into a list of words
#
# Input:  "claude is open for all"
# Output: ['claude', 'is', 'open', 'for', 'all']
#
# Approach: str.split() splits on any whitespace by default and removes
# leading/trailing spaces, making it the idiomatic way to tokenise a sentence.

mystring = "claude is open for all"

list2 = mystring.split()
print(list2)
# Output: ['claude', 'is', 'open', 'for', 'all']

# Split on a specific delimiter
csv_string = "apple,banana,cherry"
fruits = csv_string.split(",")
print(fruits)
# Output: ['apple', 'banana', 'cherry']
