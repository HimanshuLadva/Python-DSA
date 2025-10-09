class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            self.head = new_node

    def delete_node(self, key):
        current = self.head

        if not current:
            return
        
        prev=None
        while True:
            if current.data == key:
                break
            prev = current
            current = current.next

            if current == self.head:
                print("Error: key not found in list")
                return
            
        if current == self.head:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            
            if self.head == self.head.next:
                self.head = None
            else:
                last_node.next = self.head.next
                self.head = self.head.next
        else:
            prev.next = current.next
    
    def print_list(self):
        if not self.head:
            print("list is empty!")

        current = self.head

        while True:
            print(current.data, end="->" if current.next != self.head else " (head)\n")
            current = current.next
            
            if current == self.head:
                break

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.print_list()
llist.delete_node(2)
llist.print_list()
# llist.prepend(10)
# llist.print_list()

        