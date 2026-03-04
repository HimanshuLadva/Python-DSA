# https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04
from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)
        
        count = 0
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                count += get_column_sum(col_idx) == 1   
        
        return count
    # 7ms 
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    isolated = True

                    for x in range(n):
                        if mat[i][x] == 1 and x != j:
                            isolated = False
                            break

                    if isolated:
                        for y in range(m):
                            if mat[y][j] == 1 and y != i:
                                isolated = False
                                break
                    if isolated:
                        count += 1
        return count
    
sol = Solution()
mat = [[1,0,0],[0,1,0],[0,0,1]]
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(sol.numSpecial(mat))