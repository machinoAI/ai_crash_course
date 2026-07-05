# String Comparison Using ASCII / Unicode Ordinal Values
#
# Python compares strings lexicographically using the Unicode code point (ordinal)
# of each character. Uppercase letters have LOWER ordinal values than lowercase.
#
# ASCII ranges:
#   'A'–'Z' : 65–90
#   'a'–'z' : 97–122
#
# Therefore: 'a' > 'A', 'a' > 'Z', 'ravi' > 'Ravi'

name  = "ravi"
name1 = "Ravi"

print(name == name1)    # False — case-sensitive comparison
print(name >= name1)    # True  — 'r'(114) > 'R'(82)

# ASCII ordinal values
print("ord('A') =", ord('A'))   # 65
print("ord('Z') =", ord('Z'))   # 90
print("ord('a') =", ord('a'))   # 97
print("ord('z') =", ord('z'))   # 122

# chr() is the reverse of ord()
print("chr(65)  =", chr(65))    # 'A'
print("chr(97)  =", chr(97))    # 'a'

# Case-insensitive comparison
print(name.lower() == name1.lower())   # True
