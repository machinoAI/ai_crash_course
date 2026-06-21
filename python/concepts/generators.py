# A Generator is function which uses yield to produce value lazily, one at a time, making it more memory efficient
# than returning all values at once.

# Generator is useful in processing a very large file (100GB).

#Example:

def read_large_file(path):
    with open(path, "r") as file:
        for line in file:
            yield line  # Reading one line at a time



for line in read_large_file("logs.txt"):
    print(line)  # Process
