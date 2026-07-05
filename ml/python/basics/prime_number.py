
def prime_number(n, i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    return prime_number(n, i-1)


n =eval(input("Enter a number:"))

indicator = prime_number(n, n-1)
if indicator==1:
    print("prime number")

if indicator==0:
    print("Not a prime number")