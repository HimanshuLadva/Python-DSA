# https://leetcode.com/problems/left-and-right-sum-differences/?envType=daily-question&envId=2026-06-06

from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            res.append(abs(sum(nums[:i]) - sum(nums[i+1:n])))
        
        return res
    
sol = Solution()
print(sol.leftRightDifference(nums = [10,4,8,3]))