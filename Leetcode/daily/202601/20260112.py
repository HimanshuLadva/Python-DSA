# https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12
# #topic
from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            curr_x = points[i][0]
            curr_y = points[i][1]
            target_x = points[i+1][0]
            target_y = points[i+1][1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        return ans
    
sol = Solution()
points = [[1,1],[3,4],[-1,0]]
print(sol.minTimeToVisitAllPoints(points))