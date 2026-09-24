# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        return x * self.myPow(x, n - 1)

sol = Solution()
print(sol.myPow(x = 2.00000, n = 10))