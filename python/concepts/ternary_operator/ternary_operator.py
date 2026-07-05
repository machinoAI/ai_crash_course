# Ternary Operator (Conditional Expression)
#
# Syntax:  value_if_true  if  condition  else  value_if_false
#
# It is a compact one-line alternative to a full if-else block.
# Equivalent to:
#   if condition:
#       result = value_if_true
#   else:
#       result = value_if_false

def check_age(age):
    status = "18+" if age >= 18 else "under age"
    print(f"Age {age} → {status}")

check_age(20)   # Output: Age 20 → 18+
check_age(17)   # Output: Age 17 → under age

# Ternary in an expression (without a variable)
score = 75
grade = "Pass" if score >= 50 else "Fail"
print("Grade:", grade)   # Output: Grade: Pass

# Nested ternary (use sparingly — hurts readability)
marks = 85
result = "Distinction" if marks >= 80 else ("Pass" if marks >= 50 else "Fail")
print("Result:", result)  # Output: Result: Distinction
