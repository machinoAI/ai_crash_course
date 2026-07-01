from transformers import MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def find_middle(self, head):

        if head is None:
            return head

        if head.next is None:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        return slow.data



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
# node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node5

head = node1

ll = LinkedList()
mid = ll.find_middle(head)
print("mid:", mid)


