class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next

        print(llstr)

ll = Linked_list()
ll.insert_at_beg(8)
ll.insert_at_beg(10)
ll.insert_at_beg(12)
ll.print()

