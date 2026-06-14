# 5! = 5*4!
# 5*4*3!
#5*4*3*2!
#5*4*3*2*1!
#5*4*3*2*1 = 120


def factorial(n):
    if n==0:
        return 1

    return n*factorial(n-1)

print(factorial(5))