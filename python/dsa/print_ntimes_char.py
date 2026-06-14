from curses.ascii import isalpha

input_string = "a2b3c5"

#output = "aabbbccccc"

output = ""

for ch in list(input_string):
    if isalpha(ch):
        var = ch
    else:
        num = int(ch)
        output = output+(var*num)


print(output)


