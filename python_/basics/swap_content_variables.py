# Swap content of variables
a =10
b =20

print("==Method 1:==")
print("Before: ", a, b)
a, b = b, a
print("After: ", a, b)


print("==Method 2:==")
print("Before: ", a, b)
temp = a
a = b
b = temp

print("After: ", a, b)


print("==Method 3:==")
print("Before: ", a, b)
a = a+b
b = a-b
a = a- b

print("After: ", a, b)