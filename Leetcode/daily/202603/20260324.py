# https://leetcode.com/problems/construct-product-matrix/description/?envType=daily-question&envId=2026-03-24
from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid),len(grid[0])

        result = [[1]*n for _ in range(m)]

        # prefix pass
        prefix = 1
        for i in range(m):
            for j in range(n):
                result[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
            
        # suffix pass
        suffix = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1,-1):
                result[i][j] = (result[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return result
    def constructProductMatrixV1(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        result = [[1]*n for _ in range(m)]
        
        # Prefix pass
        prefix = 1
        for i in range(m):
            for j in range(n):
                result[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
        
        # Suffix pass
        suffix = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                result[i][j] = (result[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
        
        return result
    
    # TLE but best approch
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        flat = []
        for row in grid:
            flat.extend(row)

        size = len(flat)

        prefix1D = [1]*size
        for i in range(1, size):
            prefix1D[i] = prefix1D[i-1] * flat[i-1]
        
        suffix1D = [1]*size
        for i in range(size-2,-1,-1):
            suffix1D[i] = suffix1D[i+1] * flat[i+1]
        
        result = [[0] * n for _ in range(m)]
        k = 0
        for i in range(m):
            for j in range(n):
                result[i][j] = (prefix1D[k] * suffix1D[k]) % 12345
                k += 1
        
        return result
    # TLE
    def constructProductMatrixV1(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for i in range(m)]
        total_product = 1
        for i in range(m):
            for j in range(n):
                total_product *= grid[i][j]
        
        for i in range(m):
            for j in range(n):
                ans = (total_product // grid[i][j])
                result[i][j] = (ans % 12345) if ans >= 12345 else ans

        return result
    
sol = Solution()
print(sol.constructProductMatrix(grid = [[1,2],[3,4]]))
print(sol.constructProductMatrix(grid = [[12345],[2],[1]]))
print(sol.constructProductMatrix([[1,2,3],[4,5,6],[7,8,9]]))
