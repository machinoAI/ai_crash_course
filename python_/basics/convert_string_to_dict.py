# Convert a string into a dictionary by pairing consecutive words
#
# Input:  "claude is open for all people"
# Output: {'claude': 'is', 'open': 'for', 'all': 'people'}
#
# Approach: Split the string into a list, then iterate with step=2.
# Word at index i becomes the key, word at index i+1 becomes the value.
# Requires the string to have an even number of words.

mystring = "claude is open for all people"

dict1 = {}
list_string = mystring.split(" ")

for i in range(0, len(list_string), 2):
    dict1[list_string[i]] = list_string[i + 1]

print(dict1)
# Output: {'claude': 'is', 'open': 'for', 'all': 'people'}
