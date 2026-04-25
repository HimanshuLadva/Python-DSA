# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description/?envType=daily-question&envId=2026-04-25
#newlearn
from typing import List
from itertools import combinations
from math import inf
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        ans = 0

        for chosen in combinations(points, k):
            # print(chosen)
            min_dist = inf
            for i in range(k):
                for j in range(i + 1, k):
                    dist = manhattan(chosen[i], chosen[j])
                    min_dist = min(dist, min_dist)
            
            ans = max(ans, min_dist)
        return ans

sol = Solution()
print(sol.maxDistance(side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4))