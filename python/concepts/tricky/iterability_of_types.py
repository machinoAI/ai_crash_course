# Iterability of Different Python Types
#
# A type is iterable if Python can loop over it with `for`.
# int and bool are NOT iterable — trying to loop over them raises TypeError.
# Wrapping with range() or str() makes integers iterable.

# --- FAIL cases ---

# for i in 765:         # TypeError: 'int' object is not iterable
#     print(i)

# for i in (765 < 1):   # TypeError: 'bool' object is not iterable
#     print(i)

# --- PASS cases ---

# range() produces a sequence of integers → iterable
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# str() converts int to its digit characters → iterable
print("str(765):")
for ch in str(765):
    print(ch, end=" ")
print()

# Other natively iterable types
print("list   :", [x for x in [10, 20, 30]])
print("tuple  :", [x for x in (10, 20, 30)])
print("string :", [ch for ch in "hello"])
print("dict   :", [k for k in {"a": 1, "b": 2}])   # iterates over keys
