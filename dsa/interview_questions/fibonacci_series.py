"""
Given a number n, append all Fibonacci numbers up to n to a list.

n = 20

output = [0, 1, 1, 2, 3, 5, 8, 13]
"""

def fibonacci_numbers(n):

    result = []
    a,b = 0,1

    while a <=n:
        result.append(a)

        a, b = b, a+b

    return result


n = 20

print(fibonacci_numbers(n))

def fibonacci(n):

    result = []

    a,b = 0,1

    for _  in range(n):

        result.append(a)
        a, b = a, a+b

    return result