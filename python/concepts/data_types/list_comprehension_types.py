# List Comprehension — 4 Types
#
# Type 1: [ expression for variable in iterable ]
# Type 2: [ expression for variable in iterable if cond ]
# Type 3: [ expression for variable in iterable if cond1 if cond2 ]
# Type 4: [ expression if cond else other_expression for variable in iterable ]

nums = [1, 2, 3, 4, 12, 15, 30]

# Type 1 — transform every element (square each number)
square = [num * num for num in nums]
print("Type 1 — all squares        :", square)
# Output: [1, 4, 9, 16, 144, 225, 900]

# Type 2 — filter + transform (square of even numbers only)
even_square = [num * num for num in nums if num % 2 == 0]
print("Type 2 — even squares       :", even_square)
# Output: [4, 16, 144, 900]

odd_square = [num * num for num in nums if num % 2 == 1]
print("Type 2 — odd squares        :", odd_square)
# Output: [1, 9, 225]

# Type 3 — multiple conditions (must be divisible by both 2 AND 3)
divi_by_2_and_3_square = [num * num for num in nums if num % 2 == 0 if num % 3 == 0]
print("Type 3 — div by 2&3 squares :", divi_by_2_and_3_square)
# Output: [144, 900]

# Type 4 — inline if-else (cube if even, square if odd)
even_cube_odd_square = [num ** 3 if num % 2 == 0 else num ** 2 for num in nums]
print("Type 4 — cube/square mix    :", even_cube_odd_square)
# Output: [1, 8, 9, 64, 1728, 225, 27000]
