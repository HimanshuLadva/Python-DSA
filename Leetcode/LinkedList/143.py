# https://leetcode.com/problems/reorder-list?envType=problem-list-v2&envId=linked-list
# #MIMP
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        print(f"middle of list = {slow.val}")

        # Reverse last half list
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        second = prev
        start = head
        while second:
            next = start.next
            mnext = second.next

            start.next = second
            second.next = next

            second = mnext
            start = next

        """ curr = head
        while curr:
            print(curr.val, end="=>")
            curr = curr.next """

        return None
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
sol.reorderList(head)