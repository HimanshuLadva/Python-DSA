# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/?envType=daily-question&envId=2026-01-15

from typing import List
class Solution:
    def maxSpan(self, bars: List[int]):
        res = 1
        streak = 1
        for i in range(1, len(bars)):
            if bars[i] - bars[i-1] == 1:
                streak += 1
            else:
                streak = 1
            res = max(res, streak)
        
        res += 1
        return res

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        s = min(self.maxSpan(hBars), self.maxSpan(vBars))
        return s * s

    
sol = Solution()
n = 2
m = 3
hBars = [2,3]
vBars = [2,4]
print(sol.maximizeSquareHoleArea(n, m, hBars, vBars))