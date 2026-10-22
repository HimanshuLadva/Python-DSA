# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    # with Recursion Basic > Recursion → Memoization Bridge
    def fib(self, n: int) -> int:
        memo = {}
        def solve(n:int):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = solve(n-1) + solve(n-2)
            return memo[n]

        return solve(n)

    # with Recursion > Base Cases
    def fibv2(self, n: int, a:int = 0, b: int = 1) -> int:
        if n == 0:
            return a

        return self.fib(n-1, b, a+b)

    # proper fibonacci series logic
    #revision
    #howtowork
    #implogic
    def fibv2(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)

    def fibv1(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(n):
            a,b = b,a+b

        return a


sol = Solution()
print(sol.fib(6))