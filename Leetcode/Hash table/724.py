# https://leetcode.com/problems/find-pivot-index/description/

from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        prev_sum = 0

        for i, num in enumerate(nums):
            if prev_sum == all_sum - num - prev_sum:
                return i
            prev_sum += num
            
        return -1

sol = Solution()
sol.pivotIndex(nums = [1,7,3,6,5,6])