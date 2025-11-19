# https://leetcode.com/problems/keep-multiplying-found-values-by-two?envType=daily-question&envId=2025-11-19

from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original