# Positive integer that is equal to sum of it's +ve divisors , excluding the number itself.

#example: 6 = 1+2+3 ==6 ; 6 is a perfect number

def perfect_num(n):

    divisor_sum = sum(num for num in range(1, n) if n%num ==0)
    if n == divisor_sum:
        print("Number is perfect:", n)
    else:
        print("Number is not perfect:", n)

perfect_num(25)


# Find the list of perfect numbers under given number:

def find_perfect_numbers(n):

    perfect_num_list = []
    for i in range(1, n):
        divisor_sum = sum(num for num in range(1, i) if i % num == 0)
        if i == divisor_sum:
            perfect_num_list.append(i)

    return perfect_num_list

result = find_perfect_numbers(1000)
print(result)