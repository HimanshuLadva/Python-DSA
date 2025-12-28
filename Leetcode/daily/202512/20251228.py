# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix?envType=daily-question&envId=2025-12-28
# #method

from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row, col = 0, n-1
        count = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += (m - row)
                col -= 1
            else:
                row += 1
        return count
    # 4ms
    def countNegativesV1(self, grid: List[List[int]]) -> int:
        print(grid)
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    count += 1
        return count
    
sol = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(grid))