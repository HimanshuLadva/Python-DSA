# https://leetcode.com/problems/sort-list/?envType=problem-list-v2&envId=merge-sort

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, nums, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = nums[left + i]

        for j in range(n2):
            R[j] = nums[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2

            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []

        start = head
        while start:
            nums.append(start.val)
            start = start.next

        n = len(nums)

        if n == 0:
            return head
        
        self.mergeSort(nums, 0, n -1)

        new_head = ListNode(nums[0])
        start = new_head
        for i in range(1, n):
            start.next = ListNode(nums[i])
            start = start.next
        
        return new_head