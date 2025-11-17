# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        is_minus = False
        if x < 0:
            is_minus = True
            x = x*-1

        x = str(x)
        x = int(x[::-1])

        x = -x if is_minus else x
        if x > -(2 ** 31) and x < (2**31) - 1:
            return x
        return 0

sol = Solution()
x = -123
x = 1534236469
print(sol.reverse(x))