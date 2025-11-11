# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array?envType=daily-question&envId=2025-11-01
# #MIMP dummy node concept

from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        while curr:
            if curr.val in num_set:
                    prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
    
    # time limit exceed
    def modifiedListV1(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if curr.val in nums:
                if curr == head:
                    head = curr.next
                else:
                    prev.next = curr.next
                    curr = prev
            prev = curr
            curr = curr.next

        return head
    
sol = Solution()
nums = [1,2,3]
nums = [1]
nums = [1,7,6,2,4]
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(1)
# head.next.next.next.next.next = ListNode(2)
head = ListNode(3)
head.next = ListNode(7)
head.next.next = ListNode(1)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(1)
sol.modifiedList(nums, head)