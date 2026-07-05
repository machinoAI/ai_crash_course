# Walrus Operator  :=  (Assignment Expression)
# Introduced in Python 3.8
#
# Assigns a value to a variable AND returns that value — all in one expression.
# Useful for avoiding redundant computations inside conditions or loop headers.

# Basic usage: assign and use in the same expression
print((a := 100) + 1)   # Output: 101  (a is assigned 100, then 100+1 is printed)
print("a =", a)          # Output: a = 100

data = (10, 20, 30, 40, 50, 60)

# Example 1 — classic while loop (needs a separate n variable)
n = len(data)
i = 0
print("\nExample 1 — classic while loop:")
while i < n:
    print(data[i])
    i += 1

# Example 2 — walrus for n (compute len inside the condition)
i = 0
print("\nExample 2 — walrus for n:")
while i < (n := len(data)):
    print(data[i])
    i += 1

# Example 3 — walrus for both n and i (most compact)
# i starts at -1 so the first increment brings it to 0
i = -1
print("\nExample 3 — walrus for both n and i:")
while (i := i + 1) < (n := len(data)):
    print(data[i])

# Example 4 — walrus in a list comprehension filter
# Avoids calling an expensive function twice
results = [y for x in range(10) if (y := x * x) > 20]
print("\nSquares > 20:", results)
# Output: [25, 36, 49, 64, 81]
