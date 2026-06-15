# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=daily-question&envId=2026-06-15

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        mid = n // 2
        curr = head
        prev = None
        i = 0
        while i < mid:
            prev = curr
            curr = curr.next
            i += 1

        if prev:
            prev.next = curr.next
        else:
            head = None

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        return head
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)
sol.deleteMiddle(head)
    