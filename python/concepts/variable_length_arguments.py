
# Variable length arguments:
# *num -> Pass n number of arguments

def sum1(*num):
    sum=0

    for i in num:
        sum +=i
    return sum



print( sum1(10,20))
print( sum1(10,20, 30,40))
print( sum1(10,20,30,1,2,3,4))

# Variable length keyword arguments:

def sum1(**num):
    sum=0

    for key in num:
        sum +=num[key] #dictionary
    return sum


print( sum1(num1=10,num2=20))