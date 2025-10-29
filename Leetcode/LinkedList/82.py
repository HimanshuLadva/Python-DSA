# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii?envType=problem-list-v2&envId=linked-list

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = None
        second = head
        third = head.next
        while third:
            if third and second.val == third.val:
                second.next = third.next
                third = second.next
            else:
                first = second
                second = second.next
                third = third.next

        curr = head
        while curr:
            print(curr.val, end="=>")
            curr = curr.next
        print()

        return head

    def deleteDuplicatesV1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lookup = {}
        curr = head
        while curr:
            if curr.val not in lookup:
                lookup[curr.val] = 0
            lookup[curr.val] += 1
            curr = curr.next

        prev = head
        curr = head
        while curr:
            prev = curr
            curr = curr.next
            if curr and prev.val == curr.val and lookup[curr.val] > 1:
                prev.next = curr.next
                curr = prev

        curr = head
        while curr:
            print(curr.val, end="=>")
            curr = curr.next

        print()
        return head
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
sol.deleteDuplicates(head)