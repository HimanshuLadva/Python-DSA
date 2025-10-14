# https://leetcode.com/problems/remove-linked-list-elements?envType=problem-list-v2&envId=linked-list

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def append(self, data):
        cnode = ListNode(data)

        if not self.head:
            self.head = cnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = cnode
    
    def removeElements(self, val: int) -> Optional[ListNode]:
        curr = self.head
        prev = self.head
        while curr:
            if curr.val == val:
                if curr == self.head:
                    self.head = curr.next
                    curr = self.head
                    prev = curr
                else:
                    prev.next = curr.next
                    curr = prev
                    prev = curr
            else:
                prev = curr
                curr = curr.next
        return self.head
    
    def removeElementsV1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = head
        while curr:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev
            else:
                prev = curr
                curr = curr.next
        return head
    
    def display(self):
        if not self.head:
            print("list is empty")
            return
        else:
            current = self.head
            while current:
                print(current.val, end="->" if current.next else "\n")
                current = current.next
    
sol = Solution()
sol.append(1)
sol.append(2)
sol.append(2)
sol.append(1)
sol.display()
sol.removeElements(2)
sol.display()
