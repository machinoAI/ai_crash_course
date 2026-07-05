# Bitwise NOT operation:
# 1. Take any integer
# 2. Convert it to binary representation
# 3. Negate each bit (0 → 1 and 1 → 0)
# 4. Convert the resulting binary back to integer

num = int(input("Enter the number:"))
binary_num = bin(num)
binary_num = binary_num[2:]
not_binary = ""
# apply Not rule
for bit in binary_num:
    if int(bit)==0:
        not_binary =not_binary+"1"
    else:
        not_binary =not_binary+"0"


# converting back to integer from binary
sum1 = 0
for i in range(len(not_binary)):
    sum1=sum1+(int(not_binary[i]) * (2**(len(not_binary)-(i+1))))


print("binary_num:", binary_num)
print("not_binary:", not_binary)
print("New Number:", sum1)