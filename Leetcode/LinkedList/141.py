# https://leetcode.com/problems/linked-list-cycle?envType=problem-list-v2&envId=linked-list

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False
    
    def hasCycleV1(self, head: Optional[ListNode]) -> bool:
        current = head
        lookup = {}
        while current:
            current = current.next
            if current not in lookup:
                lookup[current] = 0
            lookup[current] += 1

            if lookup[current] > 1:
                return True
        return False
