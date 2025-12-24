# https://leetcode.com/problems/matrix-diagonal-sum?envType=problem-list-v2&envId=matrix

from typing import List
class Solution:
    # 0ms
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        msum = 0
        for i in range(n):
            msum += mat[i][i] + mat[i][-i-1]

        if n % 2 == 1:
            msum -= mat[n // 2][n // 2]

        return msum
    
    # 3ms
    def diagonalSumV1(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        if n != m:
            return 0
        
        msum = 0
        for i in range(n):
            if i == n-1-i:
                msum += mat[i][i]
            else:
                msum += mat[i][i] + mat[i][n-1-i] 

        return msum

sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
print(sol.diagonalSum(mat))