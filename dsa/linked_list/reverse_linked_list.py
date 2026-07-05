class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def reverse(self, head):

        if head is None:
            return head

        if head.next is None:

            return head

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev



    def traverse(self,head):
        curr = head

        while curr:
            print(curr.data)
            curr = curr.next


node1 =Node(10)
node2 =Node(20)
node3 =Node(30)
node4 =Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

ll = LinkedList()

new_head = ll.reverse(head)
ll.traverse(new_head)


