# Get the last key-value pair from a dictionary
#
# Input:  {"Sam": 300, "Musk": 400, "Ramesh": 200}
# Output: Ramesh ---> 200
#
# Approach: Convert dictionary keys to a list; use index [-1] to get the last key,
# then look up its value. Python 3.7+ dicts maintain insertion order.

student = {"Sam": 300, "Musk": 400, "Ramesh": 200}

keys_list = list(student)
last_key  = keys_list[-1]

print(last_key, "--->", student[last_key])
# Output: Ramesh ---> 200
