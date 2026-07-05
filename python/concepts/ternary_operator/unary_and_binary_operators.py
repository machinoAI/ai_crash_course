# Unary and Binary Operators
#
# Unary operator — operates on a single operand.
# Binary operator — operates on two operands.

# --- Unary Operator: Bitwise NOT (~) ---
# Rule: ~x  ==  -(x + 1)
# How it works on integers (two's complement):
#   2  in binary → 00000010
#   ~2 flips all bits → 11111101 → interpreted as -3 in two's complement
#
print("~2  =", ~2)    # Output: -3
print("~0  =", ~0)    # Output: -1
print("~-1 =", ~-1)   # Output:  0

# --- Unary Operator: Negation (-) ---
x = 5
print("-x  =", -x)    # Output: -5

# --- Binary Operators ---
a = 2
b = 3

print("a + b =", a + b)   # Addition       → 5
print("a - b =", a - b)   # Subtraction    → -1
print("a * b =", a * b)   # Multiplication → 6
print("a / b =", a / b)   # Division       → 0.666...
print("a // b =", a // b) # Floor division → 0
print("a ** b =", a ** b) # Exponentiation → 8
print("a % b =", a % b)   # Modulus        → 2
