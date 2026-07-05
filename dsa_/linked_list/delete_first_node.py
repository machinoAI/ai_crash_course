class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def delete_first_node(self, head):

        if head is None:
            return None

        head = head.next

        return head

    def traverse(self,head):
        curr = head

        while curr:
            print(curr.data)
            curr = curr.next




node1 =Node(10)
node2 =Node(20)
node3 =Node(30)

node1.next =node2
node2.next = node3
head = node1

## Delete first node
ll = LinkedList()
new_head = ll.delete_first_node(head)
ll.traverse(new_head)

