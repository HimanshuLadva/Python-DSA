# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int, a:int = 0, b:int = 1, c: int = 1) -> int:
        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c

        return self.tribonacci(n-1, b, c, a + b + c)
    
    def tribonacciV1(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        for i in range(3, n+1):
            a,b,c = b,c,a+b+c

        return [a,b,c][n] if n < 3 else c

sol = Solution()
print(sol.tribonacci(4))