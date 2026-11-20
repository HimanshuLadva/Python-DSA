# https://leetcode.com/problems/remove-linked-list-elements/

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

    # with dummy node
    #howtowork
    #revision
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

    # without dummy node
    def removeElementsV1(self, head: ListNode | None, val: int) -> ListNode | None:
        prev = head
        curr = head

        while curr:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                    curr = head
                    prev = head
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next

        # self.display(head)
        return head

sol = Solution()
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
sol.removeElements(head, 7)