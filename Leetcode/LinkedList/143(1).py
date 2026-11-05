# https://leetcode.com/problems/reorder-list/

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

    #howtowork
    #revision
    #implogic
    def reorderList(self, head: ListNode | None) -> None:
        # find middle of list
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the half list
        second = slow.next
        slow.next = None
        curr = second
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # do the main operation
        second = prev
        start = head

        while second:
            next = start.next
            mnext = second.next

            start.next = second
            second.next = next

            start = next
            second = mnext

        # self.display(head)
        return None

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
sol.reorderList(head)