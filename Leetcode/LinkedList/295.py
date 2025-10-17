# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list?envType=problem-list-v2&envId=linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow == head:
            head = None
        else:
            prev.next = slow.next

        return head
    
sol = Solution()
head = ListNode(1)
# head.next = ListNode(3)
# head.next.next = ListNode(4)
# head.next.next.next = ListNode(7)
# head.next.next.next.next = ListNode(1)
# head.next.next.next.next.next = ListNode(2)
# head.next.next.next.next.next.next = ListNode(6)
sol.deleteMiddle(head)