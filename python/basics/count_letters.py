mystring = "abbcccdddd"

#expected output : 1a2b3c4d

output = ""
char = mystring[0]
counter =0

for ch in mystring:
    if ch == char:
        counter +=1
    else:
        output = output+ str(counter) + char
        counter = 1
        char = ch

output = output+ str(counter) + char
print(output)