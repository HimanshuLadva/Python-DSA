# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k?envType=daily-question&envId=2025-11-26
# #newlearn

from typing import List
class Solution:
    # 988ms
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Use only one array for current row
        prev = [[0] * k for _ in range(n)]
        prev[0][grid[0][0] % k] = 1
        
        # Fill first row
        for j in range(1, n):
            for r in range(k):
                new_r = (r + grid[0][j]) % k
                prev[j][new_r] = (prev[j][new_r] + prev[j-1][r]) % MOD
        
        # Process remaining rows
        for i in range(1, m):
            curr = [[0] * k for _ in range(n)]
            
            # First column (only from above)
            for r in range(k):
                new_r = (r + grid[i][0]) % k
                curr[0][new_r] = prev[0][r]
            
            # Rest of columns
            for j in range(1, n):
                for r in range(k):
                    new_r = (r + grid[i][j]) % k
                    # From above + from left
                    curr[j][new_r] = (prev[j][r] + curr[j-1][r]) % MOD
            
            prev = curr
        
        return prev[n-1][0]
    # 1880ms
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # dp[i][j][r] = number of ways to reach (i,j) with remainder r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize starting cell
        dp[0][0][grid[0][0] % k] = 1
        
        # Fill first row
        for j in range(1, n):
            for r in range(k):
                if dp[0][j-1][r] > 0:
                    new_remainder = (r + grid[0][j]) % k
                    dp[0][j][new_remainder] = (dp[0][j][new_remainder] + dp[0][j-1][r]) % MOD
        
        # Fill first column
        for i in range(1, m):
            for r in range(k):
                if dp[i-1][0][r] > 0:
                    new_remainder = (r + grid[i][0]) % k
                    dp[i][0][new_remainder] = (dp[i][0][new_remainder] + dp[i-1][0][r]) % MOD
        
        # Fill rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                for r in range(k):
                    # From above
                    if dp[i-1][j][r] > 0:
                        new_remainder = (r + grid[i][j]) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i-1][j][r]) % MOD
                    
                    # From left
                    if dp[i][j-1][r] > 0:
                        new_remainder = (r + grid[i][j]) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i][j-1][r]) % MOD
        
        return dp[m-1][n-1][0]
        
    
sol = Solution()
grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3
sol.numberOfPaths(grid, k)