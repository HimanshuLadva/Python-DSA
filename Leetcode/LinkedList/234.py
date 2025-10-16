# https://leetcode.com/problems/palindrome-linked-list?envType=problem-list-v2&envId=linked-list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
    def isPalindromeV1(self, head: Optional[ListNode]) -> bool:
        curr = head
        temp = []

        while curr:
            print(curr.val, end="->")
            temp.append(curr.val)
            curr = curr.next

        start = 0
        end = len(temp) - 1

        while start <= end:
            if temp[start] != temp[end]:
                return False
            start += 1
            end -= 1

        return True

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(sol.isPalindrome(head))