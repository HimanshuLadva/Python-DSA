# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/?envType=daily-question&envId=2026-03-27
from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        org = [row[:] for row in mat]

        j = 0
        while j < k:
            for i in range(m):
                if i % 2 == 0:
                    temp = mat[i].pop(0)
                    mat[i].append(temp)
                else:
                    temp = mat[i].pop(len(mat[i]) - 1)
                    mat[i].insert(0, temp)
            # print(mat)
            j += 1
        # print(f"org = {org}")
        return org == mat

sol = Solution()
# print(sol.areSimilar(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4))
print(sol.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2))