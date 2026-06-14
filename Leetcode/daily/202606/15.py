# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=daily-question&envId=2026-06-14

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        res = []
        i = 0
        j = len(arr) - 1

        while i < j:
            res.append(arr[i] + arr[j])
            i += 1
            j -= 1
        
        # print(res)
        return max(res)
    
sol = Solution()
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
sol.pairSum(head)