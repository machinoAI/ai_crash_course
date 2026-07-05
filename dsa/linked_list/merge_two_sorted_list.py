class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def merge_list(self, list1, list2):

        dummy = Node(0)
        tail = dummy

        while list1 and list2:

            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

    def travers(self, head):
        curr = head

        while curr:
            print(curr.data)
            curr= curr.next

# Testing:

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4

list1 = node1

node10 = Node(2)
node11 = Node(4)
node12 = Node(6)

node10.next = node11
node11.next = node12

list2 = node10


ll = LinkedList()

merged_list = ll.merge_list(list1, list2)
ll.travers(merged_list)
