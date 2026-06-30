class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

   def delete_by_value(self, head, data):

    # CHeck if there is empty head
       if head is None:
           return None

    # check whether head itself is to be deleted.
       if head.data == data:
           return head.next

    # set head to prev and curr to next to head
       prev = head
       curr = head.next

       while curr:
           if curr.data == data:
               prev.next = curr.next  ## 10,20,30,40 and 30 to be deleted; then curr.data = 30; iter1: 10==30 no;  iter2: 20==30 no; iter3 30==30 yes then we need to update prev.next = Node object which holds value 40.
               break   # Now nod2 directly points to 40 and break.

           prev = curr   # update prev node with curr
           curr = curr.next # iterate

       return head


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

new_head = ll.delete_by_value(head, 30)
ll.traverse(new_head)


