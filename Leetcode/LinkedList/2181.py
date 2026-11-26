# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        # merging
        curr = head
        dummyNode = ListNode(0)
        dummy = dummyNode
        temp = 0
        while curr:
            if curr.val == 0:
                if curr != head:
                    dummy.next = ListNode(temp)
                    dummy = dummy.next
                    temp = 0
            else:
                temp += curr.val

            curr = curr.next

        return dummyNode.next
    
sol = Solution()
head = ListNode(0,
    ListNode(3,
    ListNode(1,
    ListNode(0,
    ListNode(4,
    ListNode(5,
    ListNode(2,
    ListNode(0))))))))
sol.mergeNodes(head)