# Tuple Packing and Unpacking
#
# Packing   — combining multiple values into one tuple
# Unpacking — assigning tuple elements to individual variables
#
# Key rule: Lists support packing but NOT unpacking.
#           Tuples support both packing AND unpacking.

# Packing (works for both list and tuple)
packed_tuple = ("Sam", 40, 300.0, 4+3j, "True")
packed_list  = ["Sam", 40, 300.0, 4+3j, "True"]

# Unpacking — tuple (works fine)
a, b, c, d, e = ("Sam", 40, 300.0, 4+3j, "True")
print("Unpacked from tuple:", a, b, c, d, e)

# Unpacking without parentheses also works (Python sees it as a tuple)
a, b, c, d, e = "Sam", 40, 300.0, 4+3j, "True"
print("Unpacked (no parens):", a, b, c, d, e)

# Unpacking — list (also works in Python; lists CAN be unpacked unlike the common misconception)
a, b, c, d, e = ["Sam", 40, 300.0, 4+3j, "True"]
print("Unpacked from list :", a, b, c, d, e)

# The real restriction: tuple COMPREHENSION is not natively supported.
# (generator expression in () is NOT the same as a tuple comprehension)
list_comp  = [x * 2 for x in range(5)]   # valid list comprehension
gen_expr   = tuple(x * 2 for x in range(5))  # workaround: wrap generator in tuple()
print("List comprehension :", list_comp)
print("Tuple from generator:", gen_expr)
