from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k//2):
            for j in range(k):
                print((x+i, y+j), end=" ")
            print()
            for j in range(k):
                print((x + k - i - 1, y + j), end=" ")
            print()
        
        for i in range(k // 2):
            for j in range(k):
                grid[x+i][y+j],grid[x + k - i - 1][y + j] = grid[x + k - i - 1][y + j],grid[x+i][y+j]
        return grid
    
sol = Solution()
sol.reverseSubmatrix(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3)