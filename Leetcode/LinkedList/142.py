# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                #howtowork
                #revision
                #implogic
                # for find cycle start element 
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
            
        return None

sol = Solution()
sol.detectCycle()