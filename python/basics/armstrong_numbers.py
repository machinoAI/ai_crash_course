# Python program to print armstrong numbers between 1 to 1000:

# Armstrong Number: Numbers of n digits which are equal to sum of nth power of its digits
# 27 == (2**2 + 7**2) = 53 should equal to 27 then it's called armstrong number
# 153 == ( 1**3 + 5**3 + 3**3) == 153 it is an armstrong number ; here power n=3 is coming from length of number ie 3

armstrong_num = []

for i in range(1, 1001):
    n = len(str(i))
    digits = list(str(i))
    power_sum = sum(int(num)**n for num in digits)
    if power_sum == i:
        armstrong_num.append(i)

print(armstrong_num)
