# Count the number of dictionary entries whose value is a list
#
# Input:  {'jay': [23, 'male, 200000'], 'raj': 25, 'vicky': ['male', 22], 'ram': ['male', 23]}
# Output: 3  (jay, vicky, ram have list values; raj has an int value)
#
# Approach: Extract all values, then use isinstance(item, list) to check type.

data = {
    'jay': [23, 'male, 200000'],
    'raj': 25,
    'vicky': ['male', 22],
    'ram': ['male', 23],
}

count = 0
for item in data.values():
    if isinstance(item, list):
        count += 1

print("Number of list-valued entries:", count)
# Output: Number of list-valued entries: 3
