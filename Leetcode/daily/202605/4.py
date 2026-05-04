# https://leetcode.com/problems/rotate-image/description/?envType=daily-question&envId=2026-05-04
#implogic - rotate matrix by 90 degree (modify matrix in-place)
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(zip(*matrix))
        matrix[:] = [list(row[::-1]) for row in matrix]

sol = Solution()
sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])
        