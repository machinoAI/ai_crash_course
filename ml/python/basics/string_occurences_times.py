
mystring = "abcaba"

# output = "abcaabbaaa for 2nd a, a has to print twice and for 3rd a thrice and so on...

str_dict = {}
output_string = ""

for ch in mystring:
    if ch in str_dict.keys():
        str_dict[ch] +=1
        chars = ch*str_dict[ch]
        output_string = output_string+"".join(chars)
    else:
        str_dict[ch] = 1
        chars = ch * 1
        output_string = output_string+"".join(chars)

print(output_string)




