# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/?envType=daily-question&envId=2026-08-25

from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = k
        while True:
            if i not in nums:
                return i
            
            i *= k
        return 0

sol = Solution()
sol.missingMultiple(nums = [8,2,3,4,6], k = 2)