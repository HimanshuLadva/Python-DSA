# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/?envType=daily-question&envId=2026-03-20
from typing import List
#newlearn
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = set()
                
                # collect unique elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                
                vals = sorted(vals)
                
                # if only one unique value
                if len(vals) == 1:
                    ans[i][j] = 0
                    continue
                
                # compute min diff between distinct values
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                ans[i][j] = min_diff
        
        return ans