# https://leetcode.com/problems/rotate-list?envType=problem-list-v2&envId=linked-list
# #MIMP
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        k = k % length
        if k == 0:
            return head
        
        curr.next = head

        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
    
    def rotateRightV1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        if not head:
            return head
        
        while k != count:
            curr = head
            prev = head
            while curr.next:
                prev = curr
                curr = curr.next
            
            curr.next = head
            prev.next = None
            head = curr
            count += 1

        """ curr = head
        while curr:
            print(curr.val,end="->")
            curr = curr.next """

        return head
    
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.rotateRight(head, 2)
     