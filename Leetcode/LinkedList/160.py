# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    #howtowork
    #revision
    #implogic
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        lenA = 0
        lenB = 0

        while a:
            lenA += 1
            a = a.next

        while b:
            lenB += 1
            b = b.next

        a = headA
        b = headB
        while lenA > lenB:
            lenA -= 1
            a = a.next

        while lenB > lenA:
            lenB -= 1
            b = b.next

        while a is not b:
            a = a.next if a else headA
            b = b.next if b else headB

        return a

        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 is not p2:
            p1 = p1.next if p1 else headA
            p2 = p2.next if p2 else headB

        return p1

sol = Solution()
head = ListNode(4)
head.next = ListNode(1)
head.next.next = ListNode(8)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head1 = ListNode(5)
head1.next = ListNode(6)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(8)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
sol.getIntersectionNode(head, head1)