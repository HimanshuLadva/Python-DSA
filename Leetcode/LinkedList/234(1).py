# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def display(self, head: Optional[ListNode]):
            print("------------------")
            curr = head
            while curr:
                print(curr.val)
                curr = curr.next
            print("-------------------")
            
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        back = prev
        curr = head

        while curr and back:
            if curr.val != back.val:
                return False

            curr = curr.next
            back = back.next
        
        return True

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.isPalindrome(head)