# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/?envType=daily-question&envId=2026-04-27
#newlearn
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }

        visited = [[False]*n for _ in range(m)]

        r, c = 0, 0

        while True:
            if r == m-1 and c == n-1:
                return True

            visited[r][c] = True
            moved = False

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:

                    # neighbor must connect back
                    if (-dr, -dc) in dirs[grid[nr][nc]]:
                        r, c = nr, nc
                        moved = True
                        break

            if not moved:
                return False
    
sol = Solution()
sol.hasValidPath(grid = [[2,4,3],[6,5,2]])