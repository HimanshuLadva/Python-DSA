# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    # Recursion Basic > Recursion → Memoization Bridge
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = solve(n-1) + solve(n-2)
            return memo[n]

        return solve(n+1)
        
    def climbStairsV1(self, n: int) -> int:
        if n <= 2:
            return n

        def climb(i:int, a: int, b: int):
            if i == n+1:
                return b

            return climb(i+1, b, a+b)

        return climb(3,1,2)

    def climbStairsV1(self, n: int) -> int:
        if n <= 2:
            return n

        a = 1
        b = 2

        for i in range(3, n + 1):
            a,b = b,a+b

        return b

# Stairs:  1   2   3   4   5
# Ways:    1   2   3   5   8
# ways(4) = ways(3) + ways(2)
sol = Solution()
print(sol.climbStairs(10))