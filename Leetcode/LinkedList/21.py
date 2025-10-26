# https://leetcode.com/problems/merge-two-sorted-lists?envType=problem-list-v2&envId=linked-list
# #MIMP
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy.next
    
    def mergeTwoListsV1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = list1
        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()
        new_head = None
        for x in arr:
            new_head = self.append(new_head, x)

        """ curr = new_head
        while curr:
            print(f"data = {curr.val}")
            curr = curr.next """
        return new_head
    
    def append(self,head, data):
        cnode = ListNode(data)

        if not head:
            head = cnode
        else:
            current = head
            while current.next:
                current = current.next
            current.next = cnode
        
        return head
    
sol = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
sol.mergeTwoLists(list1, list2)