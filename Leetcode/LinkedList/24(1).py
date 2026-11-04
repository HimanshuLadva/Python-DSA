# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def display(self, head: ListNode):
        print("------------------")
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
        print("-------------------")

    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        curr = head
        prev = None
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = curr
            if prev:
                prev.next = nxt
            else:
                head = nxt
            prev = curr
            curr = curr.next

        # self.display(head)
        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
sol.swapPairs(head)