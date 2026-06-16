# String Slicing — Edge Case with Conflicting Start/Stop/Step
#
# Syntax: string[start:stop:step]
# When start < stop but step is negative, Python cannot move forward
# while stepping backward — it yields an empty string instead of raising an error.
#
# Example:
#   name = "Shantanu"   (indices 0-7)
#   name[2:8:-2]
#     start=2, stop=8, step=-2
#     To go from index 2 toward index 8 you need a positive step,
#     but step is -2 (backward) → impossible → empty string

name = "Shantanu"
output = name[2:8:-2]
print(repr(output))   # Output: ''  (empty string)

# Contrast with a valid backward slice:
# start > stop with negative step works fine
output2 = name[7:2:-2]   # starts at 7 ('u'), steps backward
print(output2)             # Output: 'unt'  (indices 7→5→3)

# Full reverse
print(name[::-1])          # Output: 'unatnahS'
