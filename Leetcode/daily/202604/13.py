# https://leetcode.com/problems/minimum-distance-to-the-target-element/?envType=daily-question&envId=2026-04-13
from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        
        n = len(nums)
        i = start - 1
        j = start + 1
        while i >= 0 or j < n:
            if i >= 0 and nums[i] == target:
                return abs(start - i)
            if j < n and nums[j] == target:
                return abs(start - j)
            i -= 1
            j += 1
        return 0