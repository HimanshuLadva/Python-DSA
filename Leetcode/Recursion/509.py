# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int, a:int = 0, b: int = 1) -> int:
        if n == 0:
            return a

        return self.fib(n-1, b, a+b)

    def fibv1(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(n):
            a,b = b,a+b

        return a


sol = Solution()
print(sol.fib(3))