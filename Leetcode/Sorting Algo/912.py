# https://leetcode.com/problems/sort-an-array/?envType=problem-list-v2&envId=merge-sort

from typing import List
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
        
    def sortArray(self, nums: List[int]) -> List[int]:
        # print(nums)
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
        # print(nums)

sol = Solution()
sol.sortArray(nums = [5,2,3,1])

