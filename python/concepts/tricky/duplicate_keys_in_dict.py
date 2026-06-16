# Duplicate Keys in a Dictionary
#
# Python dictionaries do NOT raise an error for duplicate keys.
# The last value assigned to a duplicate key silently overwrites all previous ones.
# The dictionary length counts only unique keys.
#
# Example:
#   {"Jay": 89, "viru": 81, "Jay": 52}
#   "Jay" appears twice → last value (52) wins
#   len → 2  (not 3)

dict1 = {"Jay": 89, "viru": 81, "Jay": 52}

print("Dict    :", dict1)    # Output: {'Jay': 52, 'viru': 81}
print("Length  :", len(dict1))  # Output: 2

# Practical takeaway: always validate input data if keys must be unique,
# because Python will NOT warn you about overwrites.
