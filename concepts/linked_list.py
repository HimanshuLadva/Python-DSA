class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node.next = None
            return
        
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print("Error: key not found in linked list.")

        prev.next = current_node.next
        current_node = None

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

class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList1:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node1(data)

        if self.head is None:
            self.head = new_node

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node

    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data, end="->")
            curr_node = curr_node.next

    def prepend(self, data):
        new_node = Node1(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node.next = None
            return

        prev = curr_node
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            print("Error: key is not found in list")

        prev.next = curr_node.next
        curr_node = None

llist = LinkedList1()
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