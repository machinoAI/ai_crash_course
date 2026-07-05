# Floor Division (//) with Floating-Point Numbers
#
# The // operator always rounds DOWN to the nearest integer, but
# when either operand is a float the RESULT is a float (not an int).
#
# This surprises beginners who expect // to always return an int.

print(10   // 3)    # int   // int   → int   : 3
print(10.0 // 3)    # float // int   → float : 3.0
print(10   // 3.0)  # int   // float → float : 3.0
print(10.0 // 3.0)  # float // float → float : 3.0

# Negative floor division rounds toward negative infinity (not toward zero)
print(-7 // 2)      # → -4  (floor of -3.5 is -4)
print(7  // -2)     # → -4  (floor of -3.5 is -4)

# type() confirms the return type
print(type(10 // 3))    # <class 'int'>
print(type(10.0 // 3))  # <class 'float'>
