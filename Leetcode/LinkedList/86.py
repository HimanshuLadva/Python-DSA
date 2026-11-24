# https://leetcode.com/problems/partition-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_list = ListNode(0)
        high_list = ListNode(0)

        less = less_list
        high = high_list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                high.next = head
                high = high.next
            head = head.next

        high.next = None
        less.next = high_list.next
        return less_list.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
sol.partition(head, 3)