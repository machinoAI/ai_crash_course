# fibonacci: 0,1,1,2,3,5,8,13,21,34

n = int(input("Enter number of terms:"))
first = 0
second = 1

if n<=0:
    print("Pls enter positive number.")
elif n ==1:
    print("fibonacci series is:")
    print(first)
else:
    for i in range( n):
        print(first, end=" ")
        temp = first
        first = second
        second = temp + first


# with while loop:

n = int(input("\nEnter number of terms:"))
first = 0
second = 1
count =0
if n<=0:
    print("Pls enter positive number.")
elif n ==1:
    print("fibonacci series is:")
    print(first)
else:
    while count <n:
        print(first, end=" ")
        temp = first
        first = second
        second = temp + first
        count +=1


# Method2: recursion:

def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibonacci(n - 2)+fibonacci(n - 1))


n = int(input("Enter number of terms:"))
for i in range(1, n+1):
    print(fibonacci(i), end=" ")
