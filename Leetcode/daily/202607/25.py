# https://leetcode.com/problems/maximum-product-of-two-digits/description/?envType=daily-question&envId=2026-07-25

class Solution:
    def maxProduct(self, n: int) -> int:
        arr = [int(x) for x in str(n)]
        arr.sort()

        return max(arr[-1] * arr[-2], max(arr[0] * arr[-1], arr[0] * arr[1]))

sol = Solution()
print(sol.maxProduct(n = 31))
print(sol.maxProduct(n = 124))