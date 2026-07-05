
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def remove_nth_from_end(self,head, n):

        dummy = Node(0)
        dummy.next= head #0 -> 10 - > 20 ->30 ->40-> None  and n=2 ; removing 30

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next


        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next





    def traverse(self,head):
        curr = head

        while curr:
            print(curr.data)
            curr = curr.next


node1 =Node(10)
node2 =Node(20)
node3 =Node(30)
node4 =Node(40)


node1.next =node2
node2.next = node3
node3.next = node4
head = node1

ll = LinkedList()
## Delete last node

new_head = ll.remove_nth_from_end(head, 2)
ll.traverse(new_head)


