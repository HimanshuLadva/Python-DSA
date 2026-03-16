from typing import List
class Solution:
    #howtowork
    #implogic
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        results = set()

        def rhombus_sum(r, c, k):
            s = 0
            # top -> right
            for i in range(k):
                s += grid[r-k+i][c+i]
                s += grid[r+i][c+k-i]
                s += grid[r+k-i][c-i]
                s += grid[r-i][c-k+i]
            
            return s
        
        # print centers
        for i in range(m):
            for j in range(n):
                results.add(grid[i][j])

                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    results.add(rhombus_sum(i, j, k))
                    k += 1
                # print(grid[i][j], end=" ")
            # print()

        arr = sorted(results, reverse=True)
        return arr[:3]
    
sol = Solution()
grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
sol.getBiggestThree(grid)