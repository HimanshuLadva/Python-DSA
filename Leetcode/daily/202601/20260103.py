# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid?envType=daily-question&envId=2026-01-03
# #newlearn
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for row 1
        dpA, dpB = 6, 6
        
        for _ in range(2, n + 1):
            newA = (dpA * 3 + dpB * 2) % MOD
            newB = (dpA * 2 + dpB * 2) % MOD
            dpA, dpB = newA, newB
        
        return (dpA + dpB) % MOD
