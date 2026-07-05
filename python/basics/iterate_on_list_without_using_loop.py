# Iterate on list without using loop with start and end:

mylist = eval(input("Enter a list:"))
start = eval(input("Enter start index:"))
end = eval(input("Enter end index:"))

def iterate(mylist, start, end):
    if start < 0 or start >= end or  end >=len(mylist):
        return

    print(mylist[start])
    iterate(mylist, start+1, end)


iterate(mylist, start, end)