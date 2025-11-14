# https://leetcode.com/problems/increment-submatrices-by-one?envType=daily-question&envId=2025-11-14
# #newlearn-topics

from typing import List
class Solution:
    # making from leetcode hints
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2+1):
                matrix[i][c1] += 1
                if c2 + 1 < n:
                    matrix[i][c2 + 1] -= 1

        for i in range(n):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        return matrix
    # time limit exceeded
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        for x in queries:
            r1 = x[0]
            r2 = x[2]
            c1 = x[1]
            c2 = x[3]
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    matrix[i][j] += 1

        return matrix
    
sol = Solution()
n = 5
queries = [[1,1,2,2],[0,0,1,1]]
sol.rangeAddQueries(n, queries)