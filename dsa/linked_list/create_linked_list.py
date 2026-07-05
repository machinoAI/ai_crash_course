class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traverse(self, head):
        curr = head

        while curr:
            print(curr.data)
            curr = curr.next


    def count_nodes(self, head):
        curr = head
        count =0

        while curr:
            print(count, curr.data)
            curr =curr.next
            count +=1

        return count


# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
#
# print(node1.data)
# print(node1.next)
# #===========
# node1.next = node2
#
# print(node1.data)
# print(node1.next)
# print(node1.next.data)
#
# #===================
# node1.next = node2
# node2.next = node3
# print(node1.next.next.data)

# Test
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head =node1
ll = LinkedList()
ll.traverse(head)

# test count

print(ll.count_nodes(head))




