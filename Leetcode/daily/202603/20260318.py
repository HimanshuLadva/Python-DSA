# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/?envType=daily-question&envId=2026-03-18
from typing import List
class Solution:
    #newlearn
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        cols = [0] * m
        res = 0

        for i in range(n):
            row_sum = 0
            for j in range(m):
                cols[j] += grid[i][j]
                row_sum += cols[j]
                if row_sum <= k:
                    res += 1
        return res
    
sol = Solution()
print(sol.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18))