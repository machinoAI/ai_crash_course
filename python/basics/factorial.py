# 5! = 5*4!
# 5*4*3!
#5*4*3*2!
#5*4*3*2*1!
#5*4*3*2*1 = 120

n =int(input("Enter number to calculate factoria:"))

def factorial(n):
    if n==0:
        return 1

    return n*factorial(n-1)

print(factorial(n))