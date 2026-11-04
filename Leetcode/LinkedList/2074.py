# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/

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
            print(curr.val, end=" ")
            curr = curr.next
        print()
        print("-------------------")

    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
            if not head or not head.next:
                return head
    
            # self.display(head)
            count = 1
            curr = head
            prev = head
    
            while curr:
                inner = start = curr
                temp_count = 0
    
                while temp_count < count and inner:
                    # print(inner.val, end=" ")
                    end = inner
                    inner = inner.next
                    temp_count += 1
                # print() 
    
                print(count, temp_count)
                if temp_count % 2 == 0:
                    # print(f"before = {prev.val}, {curr.val}")
                    # print(f"start = {start.val}, end = {end.val}")
                    # if inner:
                    #     print(f"after = {inner.val}")
                    after = inner
                    icurr = start
                    iprev = after
    
                    while icurr != after:
                        nxt = icurr.next
                        icurr.next = iprev
                        iprev = icurr
                        icurr = nxt
    
                    if prev:
                        prev.next = end

                    prev = start
                else:
                    prev = end
                        
    
                count += 1
                    # print(f"inner = {inner.val}")
                curr = inner
    
            # self.display(head)
            return head
    
    def reverseEvenLengthGroupsWORKED(self, head: ListNode | None) -> ListNode | None:
            if not head or not head.next:
                return head
    
            # self.display(head)
            count = 1
            curr = head
            prev = head
    
            while curr:
                inner = start = curr
                temp_count = 0
    
                while temp_count < count and inner:
                    # print(inner.val, end=" ")
                    end = inner
                    inner = inner.next
                    temp_count += 1
                # print() 
    
                # print(count, temp_count)
                if temp_count % 2 == 0:
                    # print(f"before = {prev.val}, {curr.val}")
                    # print(f"start = {start.val}, end = {end.val}")
                    # if inner:
                    #     print(f"after = {inner.val}")
                    after = inner
                    icurr = start
                    iprev = after
    
                    while icurr != after:
                        nxt = icurr.next
                        icurr.next = iprev
                        iprev = icurr
                        icurr = nxt
    
                    if prev:
                        prev.next = end

                    prev = start
                else:
                    prev = end
                        
    
                count += 1
                curr = inner
    
            # self.display(head)
            return head
    
    def reverseEvenLengthGroupsV1(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        self.display(head)
        count = 1
        curr = head
        prev = head

        while curr:
            inner = start = curr
            temp_count = count

            while temp_count and inner:
                # print(inner.val, end=" ")
                end = inner
                inner = inner.next
                temp_count -= 1
            # print() 

            print(count, temp_count)
            if (count % 2 == 0 and temp_count == 0):
                # print(f"before = {prev.val}, {curr.val}")
                # print(f"start = {start.val}, end = {end.val}")
                # if inner:
                #     print(f"after = {inner.val}")
                after = inner
                icurr = start
                iprev = after

                while icurr != after:
                    nxt = icurr.next
                    icurr.next = iprev
                    iprev = icurr
                    icurr = nxt

                if prev:
                    prev.next = end
                    

            count += 1
            if inner:
                # print(f"inner = {inner.val}")
                prev = end
                curr = inner
            else:
                break

        self.display(head)
        return head

sol = Solution()
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(9)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next.next = ListNode(4)
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(0)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(5)
sol.reverseEvenLengthGroups(head)