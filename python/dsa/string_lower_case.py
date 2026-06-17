#Program to make string lower case:
from fontTools.misc.cython import returns

mystring = "CLAUDE"
list_string = list(mystring)
lower_string = ""

for char in list_string:
    ord_num = ord(char)
    lower_ord = ord_num+32
    lower_char =chr(lower_ord)
    lower_string =lower_string+lower_char


print("lower_string:", lower_string)

