# Reverse a string using three different methods
#
# Input:  "anthropic"
# Output: "ciporthtna"

mystring = "anthropic"

# Method 1: While loop — manually walk from the end to the start
i = len(mystring)
reversed_string = []
while i > 0:
    reversed_string.append(mystring[i - 1])
    i -= 1
print("while loop :", "".join(reversed_string))

# Method 2: For loop — same idea, iterate over indices in reverse
reversed_string2 = []
for j in range(len(mystring) - 1, -1, -1):
    reversed_string2.append(mystring[j])
print("for loop   :", "".join(reversed_string2))

# Method 3: Slicing — most Pythonic, single-line approach
print("slicing    :", mystring[::-1])

# Output (all three):
# while loop : ciporthtna
# for loop   : ciporthtna
# slicing    : ciporthtna
