# https://leetcode.com/problems/remove-nodes-from-linked-list/

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
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # reverse linked list
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        # remove smaller
        curr = head
        while curr and curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # reverse linked list again
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    # TLE
    def removeNodesV1(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = head
        while curr:
            temp = curr.next
            is_found = False
            while temp:
                if temp.val > curr.val:
                    is_found = True
                temp = temp.next

            if is_found:
                if curr == head:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # self.display(head)
        return head

sol = Solution()
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)
sol.removeNodes(head)