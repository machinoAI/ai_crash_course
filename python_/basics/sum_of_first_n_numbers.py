# Using recursion: Sum of first n numbers:
# n=10 , sum =55 n>=0

n = eval(input("Enter terms:"))

# Method 1:
def sum1(n):
    if n <=0:
        return n
    return n+sum1(n-1)

print(sum1(n))


# Method 2:

def sum2(n, result):
    if n==0:
        return result
    result = result+n
    return sum2(n-1, result)

print(sum2(n, result=0))