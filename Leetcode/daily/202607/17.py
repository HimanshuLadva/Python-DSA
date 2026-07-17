# https://leetcode.com/problems/sorted-gcd-pair-queries/?envType=daily-question&envId=2026-07-17

from typing import List
from itertools import combinations
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        
        return a
    
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        gcdPairs = []

        # for i in range(n):
        #     for j in range(i+1,n):
        #         gcdPairs.append(self.gcd(nums[i], nums[j]))

        for a,b in combinations(nums, 2):
            gcdPairs.append(self.gcd(a, b))
        
        gcdPairs.sort()

        # print(gcdPairs)

        res = []
        for query in queries:
            res.append(gcdPairs[query])

        return res
    
sol = Solution()
print(sol.gcdValues(nums = [2,3,4], queries = [0,2,2]))