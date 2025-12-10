# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations?envType=daily-question&envId=2025-12-10
from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        nlen = len(complexity)
        if nlen == 1:
            return 1
        
        first = complexity[0]
        for i in range(1, nlen):
            if complexity[i] <= first:
                return 0

        fac = 1
        for i in range(1, nlen):
            fac =(fac*i) % MOD
        return fac
    
sol = Solution()
complexity = [1,16,15,2,3,6]
print(sol.countPermutations(complexity))