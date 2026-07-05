# Lambda Function:

# A Function without name or anonymous function
# Memory efficient
# Fast execution


add = lambda a,b : a+b

print(add(10,20))


arithmetic = lambda a,b : (a+b, a-b)

add, subtract = arithmetic(10,30)

print(add, subtract)