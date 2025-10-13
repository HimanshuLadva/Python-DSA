# https://leetcode.com/problems/reverse-linked-list?envType=problem-list-v2&envId=linked-list
# #MIMP
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       curr = head
       prev = None
       next = None
       while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

       head = prev
       return head