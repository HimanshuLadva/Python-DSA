# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == 1 and n == 1:
            return None

        if length == n:
            return head.next

        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while curr:
            if length == n:
                prev.next = curr.next
            else:
                prev = curr

            length -= 1
            curr = curr.next

        return dummy.next  

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.removeNthFromEnd(head, 2)