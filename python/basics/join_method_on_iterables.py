# Demonstrate str.join() across different iterables: list, tuple, and dictionary
#
# Syntax: "separator".join(iterable)
# The iterable must contain string elements only.
# For dictionaries, join() iterates over keys.

# --- List ---
lang = ["Hindi", "Java", "English"]
result = "---->".join(lang)
print("list with custom separator:", result)
# Output: Hindi---->Java---->English

lang2 = ['p', 'y', 't', 'h', 'o', 'n']
print("list of chars joined:", "".join(lang2))
# Output: python

# --- Tuple ---
tup1 = ("h", "e", "l", "l", "o")
print("tuple joined:", "".join(tup1))
# Output: hello

# --- Dictionary (joins keys only) ---
country = {"India": "100", "Japan": 120, "US": 1200}
print("dict keys joined:", " ".join(country))
# Output: India Japan US
