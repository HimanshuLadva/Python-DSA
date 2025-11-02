# https://leetcode.com/problems/count-unguarded-cells-in-the-grid?envType=daily-question&envId=2025-11-02
# #MIMP

from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['x']*n for i in range(m)]
        
        # walls mark
        for x in walls:
            grid[x[0]][x[1]] = 'w'
        
        # guards mark
        for x in guards:
            grid[x[0]][x[1]] = 'g'
            
        # guards mark
        for x in guards:
            i = x[0]
            j = x[1]

            # move to top
            top = i - 1
            while top > -1 and grid[top][j] != 'g' and grid[top][j] != 'w':
                grid[top][j] = 'c'
                top -= 1
            
            # move to right
            right = j + 1
            while right < n and grid[i][right] != 'g' and grid[i][right] != 'w':
                grid[i][right] = 'c'
                right += 1

            # move to bottom
            bottom = i + 1
            while bottom < m and grid[bottom][j] != 'g' and grid[bottom][j] != 'w': 
                grid[bottom][j] = 'c'
                bottom += 1

            # move to left
            left = j - 1
            while left > -1 and grid[i][left] != 'g' and grid[i][left] != 'w':
                grid[i][left] = 'c'
                left -= 1

        count = 0
        for row in grid:
            count += row.count('x')
    
        return count
    
    # time limit exceeded
    def countUnguardedV1(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['c']*n for i in range(m)]
        
        # walls mark
        for x in walls:
            grid[x[0]][x[1]] = 'w'

        # guards mark
        for x in guards:
            i = x[0]
            j = x[1]

            # move to top
            top = i
            while top > -1:
                if grid[top][j] == 'w':
                    break
                grid[top][j] = 'g'
                top -= 1
            
            # move to right
            right = j
            while right < n:
                if grid[i][right] == 'w':
                    break
                grid[i][right] = 'g'
                right += 1

            # move to bottom
            bottom = i
            while bottom < m:
                if grid[bottom][j] == 'w':
                    break
                grid[bottom][j] = 'g'
                bottom += 1

            # move to left
            left = j
            while left > -1:
                if grid[i][left] == 'w':
                    break
                grid[i][left] = 'g'
                left -= 1

        count = 0
        for row in grid:
            count += row.count('c')
    
        return count
    
sol = Solution()
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
print(sol.countUnguarded(m,n,guards,walls))