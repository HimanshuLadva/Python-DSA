# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/?envType=daily-question&envId=2026-01-19
#topic - prefix sum, binary search
from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix sum
        rows = len(mat)
        cols = len(mat[0])   

        pref = [[0]*(cols + 1) for _ in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                pref[i][j] = (
                    mat[i-1][j-1]
                    + pref[i-1][j]
                    + pref[i][j-1]
                    - pref[i-1][j-1]
                )
        
        def can(k):
            for i in range(k, rows + 1):
                for j in range(k, cols + 1):
                    s = pref[i][j] - pref[i-k][j] - pref[i][j-k] + pref[i-k][j-k]
                    if s <= threshold:
                        return True
            return False
        
        left,right = 0, min(rows, cols)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
sol = Solution()
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
print(sol.maxSideLength(mat, 4))
