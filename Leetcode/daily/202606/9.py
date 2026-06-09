# https://leetcode.com/problems/maximum-total-subarray-value-i/?envType=daily-question&envId=2026-06-09

from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return abs(min(nums) - max(nums)) * k
    
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(n):
            for j in range(i+2, n+1):
                temp = nums[i:j]
                max_diff = max(abs(min(temp) - max(temp)), max_diff)

        return int(max_diff) * k
    
sol = Solution()
sol.maxTotalValue(nums = [4,2,5,1], k = 3)