class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def has_cycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True


        return False



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

head = node1

ll = LinkedList()

print(ll.has_cycle(head))



