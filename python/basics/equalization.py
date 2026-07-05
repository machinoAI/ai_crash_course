
# Given:
n = 5
m = 4
mystring = "abcde"
new_string_list=["abcd", "acbe", "bcdc", "acde"]

def equalization(n, m, s, t):

    counter = 0
    s1 = []   #[a,b,c,d, e]

    for ch in s:
        s1.append(ch)

        for i in range(len(s1)):
            char=s1.pop(i)

            for word in t:
                if "".join(s1)==word:
                    counter +=1

            s1.insert(i,char)

    return counter


match_counter= equalization(n, m, mystring, new_string_list)
print(match_counter)

