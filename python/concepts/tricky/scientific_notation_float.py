# Scientific Notation in Python (E-notation)
#
# Python accepts numeric literals in scientific notation using E or e.
# The result is always a float, regardless of whether the exponent is positive or negative.
#
# Syntax:  <mantissa>E<exponent>  →  mantissa × 10^exponent

num = 2E3       # 2 × 10^3 = 2000.0
print(num)              # Output: 2000.0
print(type(num))        # Output: <class 'float'>

print(1.5E2)    # 1.5 × 10^2 = 150.0
print(3E-4)     # 3 × 10^-4  = 0.0003
print(2.5e6)    # lowercase 'e' also works → 2500000.0

# Useful in scientific computing to express very large or very small constants
speed_of_light = 3E8        # 300,000,000 m/s
electron_charge = 1.6E-19   # 0.00000000000000000016 coulombs
print("Speed of light  :", speed_of_light)
print("Electron charge :", electron_charge)
