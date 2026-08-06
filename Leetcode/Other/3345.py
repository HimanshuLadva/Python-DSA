# https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=daily-question&envId=2026-08-06

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+11):
            temp = 1
            curr = i
            while curr > 0:
                temp *= (curr % 10)
                curr //= 10

            if temp % t == 0:
                return i
            
        return 0

sol = Solution()
sol.smallestNumber(n = 10, t = 2)