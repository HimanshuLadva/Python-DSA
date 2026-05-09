# https://leetcode.com/problems/cyclically-rotating-a-grid/description/?envType=daily-question&envId=2026-05-09

from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                # print(grid[i][j], end=" ")
                print((i, j), end=" ")
            print()
        return [[]]
    
sol = Solution()
sol.rotateGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)