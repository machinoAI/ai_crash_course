class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def insert_at_end(self, head, data):
        new_node = Node(data)

        if head is None:
            return new_node

        curr = head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        return head


    def travere(self, head):

        curr = head

        while curr:
            print(curr.data)
            curr = curr.next


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
head = node1

ll = LinkedList()
ll.insert_at_end(head, 100)
ll.travere(head)