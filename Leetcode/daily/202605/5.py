# https://leetcode.com/problems/rotate-list/?envType=daily-question&envId=2026-05-05

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#revision
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        #implogic
        n = 0
        temp = head 
        while temp:
            temp = temp.next
            n += 1
        
        #If an operation repeats in cycles, only the remainder matters.
        k = k % n

        while k > 0:
            curr = head
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next
            
            if curr == head:
                return head
            prev.next = None
            curr.next = head
            head = curr
            k -= 1
        
        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        while k > 0:
            curr = head
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next
            
            if curr == head:
                return head
            prev.next = None
            curr.next = head
            head = curr
            k -= 1
            
        return head