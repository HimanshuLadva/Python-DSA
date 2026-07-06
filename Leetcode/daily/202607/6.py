# https://leetcode.com/problems/remove-covered-intervals/description/?envType=daily-question&envId=2026-07-06

from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        
        n = len(intervals)

        prev_y = intervals[0][1]
        count = n
        for i in range(1, n):
            curr_y = intervals[i][1]

            if prev_y >= curr_y:
                count -= 1
            else:
                prev_y = curr_y

        return count
    
sol = Solution()
# sol.removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]])
print(sol.removeCoveredIntervals(intervals = [[1,2],[1,4],[3,4]]))