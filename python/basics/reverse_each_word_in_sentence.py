# Reverse each word individually within a sentence (keep word order intact)
#
# Input:  "python is the goal"
# Output: "nohtyp si eht laog"
#
# Approach: Split sentence into words, reverse each word using slicing [::-1],
# then rejoin with spaces.

input_str = "python is the goal"

final_output = []
for token in input_str.split():
    rev_token = token[::-1]
    final_output.append(rev_token)

print(" ".join(final_output))
# Output: nohtyp si eht laog

# One-liner equivalent using list comprehension:
print(" ".join(word[::-1] for word in input_str.split()))
