# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/?envType=daily-question&envId=2026-02-28
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b = ''
        MOD = 10**9 + 7
        for i in range(1, n+1):
            b += f"{i:b}"

        return int(b, 2) % MOD
    
sol = Solution()
sol.concatenatedBinary(1)