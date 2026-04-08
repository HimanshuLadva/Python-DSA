# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/?envType=daily-question&envId=2026-04-08
from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        arr = nums[:]

        for l,r,k,v in queries:
            for i in range(l, r+1, k):
                arr[i] = (arr[i] * v) % MOD
        
        res = 0
        for num in arr:
            res ^= num

        return res
    # 1712ms
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l,r,k,v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (MOD)
                idx += k
        
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
    
sol = Solution()
print(sol.xorAfterQueries(nums = [1,1,1], queries = [[0,2,1,4]]))
print(sol.xorAfterQueries(nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]))