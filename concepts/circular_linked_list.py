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
        if current and current.data == key:
            self.head = current.next
            current = None
        else:
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

            if current is None:
                print("Error: key is not found in list")
            else:
                prev.next = current.next
                current = None
    
    def print_list(self):
        current = self.head

        while current.next != self.head:
            print(current.data, end="->")
            current = current.next

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
llist.prepend(10)
llist.print_list()

        