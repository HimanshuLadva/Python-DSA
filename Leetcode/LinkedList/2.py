# https://leetcode.com/problems/add-two-numbers?envType=problem-list-v2&envId=linked-list

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len_l1 = 0
        len_l2 = 0
        temp1 = l1
        while temp1.next:
            len_l1 += 1
            temp1 = temp1.next
        
        temp2 = l2
        while temp2.next:
            len_l2 += 1
            temp2 = temp2.next
        
        if len_l1 > len_l2:
            diff = len_l1 - len_l2

            while diff:
                nnode = ListNode(0)
                temp2.next = nnode
                temp2 = temp2.next
                diff -= 1
        else:
            diff = len_l2 - len_l1

            while diff:
                nnode = ListNode(0)
                temp1.next = nnode
                temp1 = temp1.next
                diff -= 1

        first = l1
        second = l2
        sumlist = None
        carry = 0
        while first:
            res = first.val + second.val + carry
            carry = 0
            nnode:ListNode

            if res > 9:
                nnode = ListNode(res % 10)
                carry = 1
            else:
                nnode = ListNode(res)

            if not sumlist:
                sumlist = nnode
            else:
                curr = sumlist
                while curr.next:
                    curr = curr.next
                curr.next = nnode

            first = first.next
            second = second.next
        
        if carry:
            curr = sumlist
            while curr.next:
                curr = curr.next
            
            curr.next = ListNode(1)

        """ print("list 1")
        curr = l1
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print()

        print("list 2")
        curr = l2
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print()

        print("list 3")
        curr = sumlist
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print() """
        return sumlist
    
sol = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
sol.addTwoNumbers(l1, l2)
