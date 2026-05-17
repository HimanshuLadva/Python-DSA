# https://leetcode.com/problems/jump-game-iii/?envType=daily-question&envId=2026-05-17

from typing import List
from math import inf
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        #revision
        #learntopic - dfs
        def dfs(i):
            if i < 0 or i >= n or i in visited:
                return False
            
            if arr[i] == 0:
                return True
            
            visited.add(i)
            
            return dfs(i + arr[i]) or dfs(i - arr[i])
        
        return dfs(start)
    
    def canReachV1(self, arr: List[int], start: int) -> bool:
        zero_idx = [i for i,x in enumerate(arr) if x == 0]
        
        n = len(arr)
        i = n
        curr = start
        while i > -1:
            if curr in zero_idx:
                return True
            
            nearest = inf
            nearest_idx = inf
            for idx in zero_idx:
                if abs(idx - curr) < nearest:
                    nearest = abs(idx - curr)
                    nearest_idx = idx

            if nearest_idx > curr:
                curr += arr[curr]
            else:
                curr -= arr[curr]
            
            i -= 1
            
        return False
    
sol = Solution()
print(sol.canReach(arr = [4,2,3,0,3,1,2], start = 5))
print(sol.canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(sol.canReach(arr = [3,0,2,1,2], start = 2))