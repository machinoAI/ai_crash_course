# Print name 10 times without using loop or manually:
count =1
def printer(name):
    global  count
    if count<= 10:
        print(name)
        count +=1
        printer(name)

printer("Claude")