# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        curr = head
        count = 0
        start = None
        end = None
        before = None
        after = None

        while curr:
            count += 1

            if count == left - 1:
                before = curr

            if count == left:
                start = curr
            if count == right:
                end = curr
                break

            curr = curr.next

        after = end.next

        curr = start
        prev = after

        #howtowork
        #revision
        #implogic
        while curr != after:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        if before:
            before.next = end
            return head

        return end


sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.reverseBetween(head, 2, 4)