# https://leetcode.com/problems/minimum-absolute-difference/description/?envType=daily-question&envId=2026-01-26
from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        
        for i in range(len(arr)-1):
            min_diff = min(min_diff,arr[i+1] - arr[i])

        ans = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i+1]])

        return ans
    
sol = Solution()
arr = [4,2,1,3]
arr = [40,11,26,27,-20]
print(sol.minimumAbsDifference(arr))