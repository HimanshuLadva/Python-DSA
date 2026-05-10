# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/?envType=daily-question&envId=2026-05-10

from typing import List
from math import inf
from functools import cache
#revision
#learntopic-dp,dfs,graph
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i: int):
            if i == n-1:
                return 0
            
            res = -inf
            for j in range(i+1, n):
                if -target <= nums[j] - nums[i] <= target:
                    res = max(res, dfs(j) + 1)
            return res
        
        ans = dfs(0)
        return -1 if ans < 0 else ans
    
    #TLE
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def solve(i, jumps):
            if i == n-1:
                return jumps
            
            maxi = -1
            j = i + 1

            while j < n:
                if -target <= nums[j] - nums[i] <= target:
                    maxi = max(maxi, solve(j, jumps+1))
                j += 1
            
            return maxi
        
        return solve(0, 0)

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        print(f"nums = {nums}")
        print(f"total = {n}")
        # -target <= nums[j] - nums[i] <= target
        i = 0
        curr = 0
        idx = 0
        while i < n:
            j = i + 1

            is_changed = False
            while j < n:
                if -target <= nums[j] - nums[i] <= target:
                    print(f"j = {j}, i = {i}, diff = {nums[j] - nums[i]}")
                    curr += 1
                    i = j
                    idx = j
                    is_changed = True

                j += 1
            
            if not is_changed:
                i += 1
            
            print(f"i = {i}")
        print(f"idx = {idx}, curr = {curr}")

        if idx != n - 1:
            return -1
        elif -target <= nums[n-1] - nums[0] <= target:
            return max(curr, 1)
        else:
            return curr
    
sol = Solution()
# print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 2))
# print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 3))
# print(sol.maximumJumps(nums = [1,3,6,4,1,2], target = 0))
# print(sol.maximumJumps(nums = [1,0,2], target = 1))
print(sol.maximumJumps(nums = [1,0,3,2], target = 1))