from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        # print(arr)

        while k != 0:
            arr.insert(0,arr.pop())
            k -= 1
        
        # print(arr)

        new_grid = [[0] * n for i in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                new_grid[i][j] = arr[count]
                count += 1

        # print(new_grid)
        return new_grid
    
sol = Solution()
sol.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)