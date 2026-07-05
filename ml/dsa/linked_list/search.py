class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def search(self, head, target):
        curr = head

        while curr:
            if curr.data == target:
                return True

            curr = curr.next
        return False

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

ll = LinkedList()
print(ll.search(head, 20))

