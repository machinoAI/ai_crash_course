class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def insert_at_beginning(self, head, data):
        #create a new node:
        new_node = Node(data)

        # point new node to current head
        new_node.next = head

        # Make new node to new head
        head = new_node

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
# ll.travere(head)
head = ll.insert_at_beginning(head, 50)
ll.travere(head)




