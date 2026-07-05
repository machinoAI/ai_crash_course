class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def delete_last_end(self,head):
        if head is None:
            return None

        if head.next is None:
            return None

        curr = head

        while curr.next.next:
            curr = curr.next

        curr.next = None
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

ll = LinkedList()
## Delete last node

new_head = ll.delete_last_end(head)
ll.traverse(new_head)


