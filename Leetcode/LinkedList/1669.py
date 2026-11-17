# https://leetcode.com/problems/merge-in-between-linked-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 0
        curr = list1
        start = None
        end = None
        while curr:
            if idx == a-1:
                start = curr
            if idx == b+1:
                end = curr
                break
            idx += 1
            curr = curr.next

        if start and end:
            start.next = list2
            curr = list2
            while curr.next:
                curr = curr.next

            curr.next = end
            
        return list1

sol = Solution()