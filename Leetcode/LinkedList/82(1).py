# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        lookup = {}
        curr = head
        while curr:
            lookup[curr.val] = lookup.get(curr.val, 0) + 1
            curr = curr.next

        curr = head
        dummy = ListNode(0, head)
        prev = dummy
        while curr:
            if lookup[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
sol.deleteDuplicates(head)