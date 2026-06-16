# Merge / append elements of one list into another using extend()
#
# Input:
#   age  = [10, 30, 90, 60, 40, 50]
#   name = ["Ramesh", "Ram", "Shohan", "Sam", "Andre", "Jose"]
#
# Output: [10, 30, 90, 60, 40, 50, 'Ramesh', 'Ram', 'Shohan', 'Sam', 'Andre', 'Jose']
#
# list.extend(iterable) adds each element of the iterable to the end of the list
# (unlike list.append() which would add the entire list as a single element).

age  = [10, 30, 90, 60, 40, 50]
name = ["Ramesh", "Ram", "Shohan", "Sam", "Andre", "Jose"]

age.extend(name)

print(age)
# Output: [10, 30, 90, 60, 40, 50, 'Ramesh', 'Ram', 'Shohan', 'Sam', 'Andre', 'Jose']
