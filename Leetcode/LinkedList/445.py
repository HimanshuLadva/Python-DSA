# https://leetcode.com/problems/add-two-numbers-ii/description/

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

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # reverse first list
        prev = None
        curr = l1
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1 = prev

        # reverse second list
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l2 = prev

        a = l1
        b = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while a and b:
            temp = a.val + b.val + carry
            if temp > 9:
                curr.next = ListNode(temp % 10)
                carry = 1
            else:
                carry = 0
                curr.next = ListNode(temp)

            curr = curr.next
            a = a.next
            b = b.next

        while a:
            temp = a.val + carry
            if temp > 9:
                curr.next = ListNode(temp % 10)
                carry = 1
            else:
                carry = 0
                curr.next = ListNode(temp)
            curr = curr.next
            a = a.next

        while b:
            temp = b.val + carry
            if temp > 9:
                curr.next = ListNode(temp % 10)
                carry = 1
            else:
                carry = 0
                curr.next = ListNode(temp)
            curr = curr.next
            b = b.next

        if carry:
            curr.next = ListNode(1)

        curr = dummy
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        dummy = prev

        # self.display(dummy.next)
        return dummy.next

sol = Solution()
# l1 = [2, 4, 3]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# l2 = [5, 6, 4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol.addTwoNumbers(l1,l2)