# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20
from typing import List
from collections import defaultdict
from math import inf
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        d1 = 0
        for i in range(n - 1, -1, -1):
            if colors[0] != colors[i]:
                d1 = i
                break
        
        d2 = 0
        for i in range(n):
            if colors[-1] != colors[i]:
                print(f"idx = {i}, {n - 1 - i}")
                d2 = n - 1 - i
                break
        
        return max(d1, d2)
    # 8ms
    def maxDistanceV1(self, colors: List[int]) -> int:
        n = len(colors)
        ans = -inf
        for i in range(n):
            for j in range(i + 1,n):
                if colors[i] != colors[j]:
                    ans = max(ans, abs(i - j))
        return ans
    
sol = Solution()
sol.maxDistance(colors = [1,1,6,1,1,1,1])