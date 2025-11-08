# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero?envType=daily-question&envId=2025-11-08
# #newlearn

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n = n>>1
        result = 0
        while n:
            result ^= n
            n >>= 1
        return result
    
sol = Solution()
n = 13
sol.minimumOneBitOperations(n)