
# sort vs sorted
"""
sort:
    - sort is a method of list
    - syntax: list.sort((key=None, reverse=False)
    - It modifies the existing list

sorted:
    - sorted works with list, tuple, dictionary etc.
    - syntax: sorted(list, key=None, reverse=false)
    - It returns a new list


"""

list1 = [1,5,8,2,0,7]

# list1.sort()
# print(list1)


sorted_list =sorted(list1)
# print("sorted_list", sorted_list)
# print(sorted(list1, reverse=True))

my_list = [(20,10), (-1,99), (8,-5), (2,7)]

print(sorted(my_list, reverse=True))  # sorting on the first item in tuple

def my_function(lst):
    return [lst[1]]

print(sorted(my_list, reverse=True, key=my_function))  # sorting on the second item in tuple