# https://leetcode.com/problems/maximum-matrix-sum?envType=daily-question&envId=2026-01-05

from typing import List
class Solution:
    # 29ms
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m_sum = 0
        n_neg = 0
        least_abs = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    n_neg += 1
                    x = -x
                
                if x < least_abs:
                    least_abs = x
                
                m_sum += x
        
        if n_neg % 2 == 0:
            return m_sum
        else:
            return m_sum - least_abs * 2
        
    # 49ms
    def maxMatrixSumV1(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        negative_count = 0
        m_sum = 0
        smallest_neg = float('inf')
        for i in range(m):
            for j in range(m):
                temp = abs(matrix[i][j])
                if temp < smallest_neg:
                    smallest_neg = temp
                m_sum += temp
                if matrix[i][j] < 0:
                    negative_count += 1
        
        if negative_count % 2 != 0:
            m_sum -= 2 * smallest_neg
        return m_sum
    
sol = Solution()
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(sol.maxMatrixSum(matrix))