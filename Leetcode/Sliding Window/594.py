# https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=sliding-window

from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left = 0
        best = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                best = max(best, right - left + 1)

        return best
    
sol = Solution()
sol.findLHS(nums = [1,3,2,2,5,2,3,7])