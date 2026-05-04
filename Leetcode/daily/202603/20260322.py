# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/?envType=daily-question&envId=2026-03-22
from typing import List
#implogic
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        for i in range(4):
            mat = list(zip(*mat))
            mat = [list(row[::-1]) for row in mat]

            if mat == target:
                return True

        return False
    
sol = Solution()
# sol.findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]])
sol.findRotation(mat = [[1,2,3],[4,5,6],[7,8,9]], target = [[7,4,1],[8,5,2],[9,6,3]])
