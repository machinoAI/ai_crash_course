# List vs Tuple — Key Differences
#
# | Property       | List               | Tuple                      |
# |----------------|--------------------|----------------------------|
# | Syntax         | [ ]  required      | ( ) optional               |
# | Mutability     | Mutable (editable) | Immutable (read-only)      |
# | Memory         | Higher             | Lower                      |
# | Speed          | Slower             | Faster                     |
# | Comprehension  | Supported          | Not supported              |
# | Unpacking      | Not supported      | Supported                  |

import sys

my_list  = ["Sam", 40, 300.0, 4+3j, "True"]   # [] is compulsory
my_tuple = ("Sam", 40, 300.0, 4+3j, "True")   # () is optional
my_tuple2 = "Sam", 40, 300.0, 4+3j, "True"    # parentheses omitted — still a tuple

# Mutability: list allows item assignment, tuple does not
my_list[1] = 38
print("Updated list:", my_list)

# my_tuple[1] = 35   # ← raises TypeError: 'tuple' object does not support item assignment

# Memory comparison
print("List  size (bytes):", sys.getsizeof(my_list))
print("Tuple size (bytes):", sys.getsizeof(my_tuple))
# Tuple is always smaller than an equivalent list
