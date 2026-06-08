# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2026-06-08

from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        min_list = []
        max_list = []
        same_list = []

        for num in nums:
            if num == pivot:
                same_list.append(num)
            elif num < pivot:
                min_list.append(num)
            else:
                max_list.append(num)
        return min_list + same_list + max_list
    
sol = Solution()
print(sol.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))