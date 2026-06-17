# Twin prime numbers: Any two prime number with difference of 2; example 11,13 are twin prime. 17 & 19 are twin


def isPrime(num):
    if num <=1:
        return False
    for i in range(2, num-1):
        if num%i==0:
            return False

    return  True


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if isPrime(num1) and isPrime(num2):
    if abs(num1-num2)==2:
        print(f"{num1} and {num2} are twin prime numbers")
    else:
        print(f"{num1} and {num2} are not twin prime numbers")
else:
    print(f"{num1} and {num2} are not twin prime numbers")