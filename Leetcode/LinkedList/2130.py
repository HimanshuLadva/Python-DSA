# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        curr = head

        while curr:
            ans.append(curr.val)
            curr = curr.next

        res = []
        i = 0
        j = len(ans) - 1

        while i < j:
            res.append(ans[i] + ans[j])
            i += 1
            j -= 1

        return max(res)