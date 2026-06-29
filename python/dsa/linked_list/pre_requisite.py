
# Example1:

a =[1,2]
b=a

b.append(3)
print(b)

# Example 2: Class & Objects
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Example 3:
head = None # Means the list is empty


# Example 4: Traversing with a Pointer

curr = head

while curr:
     print(curr.val)
     curr = curr.next

# Example 5: Never lose the next node.
temp = curr.next

# Example 6: Multiple pointers
prev =0
curr =1
next= 2

