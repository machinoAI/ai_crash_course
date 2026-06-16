# Find all duplicate elements in a list (elements that appear more than once)
#
# Input:  [10, 20, 20, 30, 40, 10, 50, 70, 40, "Ramesh"]
# Output: [20, 10, 40]
#
# Approach: Iterate through the list; if an element's count > 1 and it hasn't
# been added to the result yet, record it.

list1 = [10, 20, 20, 30, 40, 10, 50, 70, 40, "Ramesh"]
result = []

for item in list1:
    if list1.count(item) > 1:
        if item not in result:
            result.append(item)

print(result)
# Output: [20, 10, 40]
