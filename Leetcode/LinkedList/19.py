# https://leetcode.com/problems/remove-nth-node-from-end-of-list?envType=problem-list-v2&envId=linked-list

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev

        count = 0
        curr = head
        prev = head
        while curr:
            count += 1
            if count == n:
                break
            prev = curr
            curr = curr.next
        
        if curr == head:
            head = curr.next
            curr = None
        else:
            prev.next = curr.next

        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
sol.removeNthFromEnd(head, 1)