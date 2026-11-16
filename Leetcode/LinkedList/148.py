# https://leetcode.com/problems/sort-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, arr: list[int], left: int, mid: int, right: int):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]

        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr: list[int], left: int, right: int):

        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid+1, right)
            self.merge(arr, left, mid, right)

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        print("first", arr)
        self.mergeSort(arr, 0, len(arr)-1)
        print("second", arr)

        new_head = ListNode(arr[0])
        curr = new_head
        for ele in arr[1:]:
            curr.next = ListNode(ele)
            curr = curr.next

        head = new_head
        return head

sol = Solution()
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(5)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)
sol.sortList(head)