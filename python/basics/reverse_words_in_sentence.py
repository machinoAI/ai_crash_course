# Reverse words in a sentence
#
# Input:  "sky is blue"
# Output: "blue is sky"
#
# Approach: Split sentence into words, reverse the list, join back.

input_str = "sky is blue"

# Method 1: Using while loop with walrus operator
l = input_str.split(" ")
i = len(l)
new_l = []
while (i := i - 1) >= 0:
    new_l.append(l[i])

print("while loop:", " ".join(new_l))

# Method 2: Using reversed()
print("reversed():", " ".join(reversed(input_str.split(" "))))

# Method 3: Slicing [::-1]
reversed_output = " ".join(input_str.split(" ")[::-1])
print("slicing:   ", reversed_output)
