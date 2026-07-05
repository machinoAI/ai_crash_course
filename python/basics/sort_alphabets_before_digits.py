# Sort a mixed alphanumeric string so that alphabets come first (sorted),
# followed by digits (sorted)
#
# Input:  "A7R1B3"
# Output: "ABR137"
#
# Approach: Separate characters into two buckets (alpha vs digit),
# sort each bucket independently, then concatenate.

mystring = "A7R1B3"

char_list = []
num_list  = []

for char in mystring:
    if char.isalpha():
        char_list.append(char)
    else:
        num_list.append(char)

final_list = sorted(char_list) + sorted(num_list)

print(final_list)           # Output: ['A', 'B', 'R', '1', '3', '7']
print("".join(final_list))  # Output: ABR137
