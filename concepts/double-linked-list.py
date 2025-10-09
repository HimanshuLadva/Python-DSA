class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        cnode = Node(data)

        if not self.head:
            self.head = cnode
            self.tail = cnode
        else:
            self.tail.next = cnode
            cnode.prev = self.tail
            self.tail = cnode
    
    def delete(self, key):
        if not self.head:
            print("list is empty")
            return
        else:
            current = self.head
            while current and current.data != key:
                current = current.next
                if current.next == self.tail:
                    print("Error: key not found in list")
                    return
                
            current.next.prev = current.prev
            current.prev.next = current.next
            current = None

    def prepend(self, data):
        cnode = Node(data)

        if not self.head:
            self.head = cnode
            self.tail = cnode
        else:
            cnode.next = self.head
            self.head.prev = cnode
            self.head = cnode
        
    def displayf(self):
        if not self.head:
            print("list is empty")
            return 
        else:
            current = self.head
            while current:
                print(current.data, end="->" if current.next else "\n")
                current = current.next
        
    def displayb(self):
        if not self.head:
            print("list is empty")
            return 
        else:
            current = self.tail
            while current:
                print(current.data, end="->" if current.prev else "\n")
                current = current.prev

lst = DLinkedList()
lst.append(1)    
lst.append(2)    
lst.append(3)    
lst.append(4)    
lst.append(5)    
lst.append(6)
lst.displayf()
lst.delete(2)
lst.displayf() 
lst.prepend(11)
# lst.prepend(12)
lst.displayb()
lst.displayf()
