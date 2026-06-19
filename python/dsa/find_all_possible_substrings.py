
mystring = "hi!"
#output: #[H,i,!, Hi, H!, Hi!]

def find_substrings(mystring):
    s1=[]

    for i in range(0, len(mystring)):
       for j in range(i+1, len(mystring)+1):
            s1.append(mystring[i:j])

    return s1


print(find_substrings(mystring))