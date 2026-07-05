# Count the number of vowels in a string (case-insensitive)
#
# Input:  "Claude Code"
# Output: 4  (a, u, e, o, e — note: uppercase vowels like 'C' are skipped;
#              only lowercase vowels 'a','e','i','o','u' are matched here)
#
# Approach: Iterate over each character; check membership in the vowel set.

mystring = "Claude Code"

count = 0
for char in mystring:
    if char in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print("Vowel count:", count)
# Output: Vowel count: 4

# Case-insensitive version using lower():
count_ci = sum(1 for char in mystring if char.lower() in ('a', 'e', 'i', 'o', 'u'))
print("Vowel count (case-insensitive):", count_ci)
# Output: Vowel count (case-insensitive): 4
