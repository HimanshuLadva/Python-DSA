# https://leetcode.com/problems/swap-nodes-in-pairs?envType=problem-list-v2&envId=linked-list
# #pending

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head
        while curr:
            prev = curr
            curr = curr.next

            prev.next = curr.next
            curr.next = prev

        curr = head
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print()
        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
sol.swapPairs(head)