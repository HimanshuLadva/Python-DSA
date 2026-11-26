# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #howtowork
    #revision
    #implogic
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        hash_map = {}
        prefix = 0
        dummy = ListNode(0, head)

        curr = dummy
        while curr:
            prefix += curr.val
            hash_map[prefix] = curr
            curr = curr.next

        curr = dummy
        prefix = 0
        while curr:
            prefix += curr.val
            curr.next = hash_map[prefix].next
            curr = curr.next

        return dummy.next

sol = Solution()
sol.removeZeroSumSublists()