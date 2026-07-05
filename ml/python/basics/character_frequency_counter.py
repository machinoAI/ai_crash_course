# Count frequency of each character in a comma-separated string
#
# Input:  "a,a,a,b,b,c,c,c"
# Output: "a:3, b:2, c:3"
#
# Approach: Track already-visited characters to avoid duplicates,
# use str.count() to find occurrences of each unique character.

mystring = "a,a,a,b,b,c,c,c"

new_list = []
visited = []

for char in mystring.split(","):
    if char not in visited:
        new_list.append(f"{char}:{mystring.count(char)}")
        visited.append(char)

print(",".join(new_list))
# Output: a:3,b:2,c:3
