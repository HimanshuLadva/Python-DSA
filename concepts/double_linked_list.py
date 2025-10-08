class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def delete_node(self, key):
        current = self.head

        while current and current.data != key:
            current = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def print_backword(self):
        current = self.tail
        while current:
            print(current.data, end="->")
            current = current.prev
        print("None")
            
llst = LinkedList()
llst.append(1)
llst.append(2)
llst.append(3)
llst.append(4)
llst.append(5)
llst.print_forward()
llst.delete_node(2)
llst.print_forward()
llst.prepend(11)
llst.print_forward()