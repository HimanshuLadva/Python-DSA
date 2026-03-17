# https://leetcode.com/problems/largest-submatrix-with-rearrangements/?envType=daily-question&envId=2026-03-17
from typing import List
#newlearn
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        height = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    height[i][j] = height[i-1][j] + 1
                else:
                    height[i][j] = 0
        
        ans = 0
        for row in height:
            row.sort(reverse=True)
            for i,h in enumerate(row):
                ans = max(ans, h * (i + 1))

        return ans
    
sol = Solution()
matrix = [[0,0,1],[1,1,1],[1,0,1]]
sol.largestSubmatrix(matrix)