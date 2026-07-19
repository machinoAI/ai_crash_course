"""
get() method in python:
"""

employee = {"name":"Bob", "Age": 25, "salary":4000}

# Accessing via key:

print(employee["salary"])
    # output = 4000

# Accessing with wrong key:
# print(employee["sal"])  # KeyError: 'sal'

# dict.get(key, "default value")

print(employee.get("salary", "Not found"))
print(employee.get("sal", "Not found"))
print(employee.get("sal"))

if employee.get("salary", "Not found"):
    print("800 Questions still left")

