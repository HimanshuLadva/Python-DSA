# https://leetcode.com/problems/max-dot-product-of-two-subsequences?envType=daily-question&envId=2026-01-08
# #newlearn
from typing import List
from functools import lru_cache
import math
class Solution:
    def maxDotProduct(self, nums1, nums2):
        # Get the lengths of both arrays
        m, n = len(nums1), len(nums2)
        min_axis = 0 if m < n else 1
        min_size = min(m, n)
        max_size = max(m, n)
        nums = (nums1, nums2)

        dp = [[float('-inf')] * (min_size + 1) for _ in range(2)]
      
        # Iterate through each element in nums1
        for j in range(1, max_size + 1):
            for i in range(1, min_size + 1):
                j2 = j%2
                current_product = nums[min_axis][i - 1] * nums[1-min_axis][j - 1]
                dp[j2][i] = max(
                    dp[j2][i - 1],                                    # Skip nums1[i-1]
                    dp[1 - j2][i],                                    # Skip nums2[j-1]
                    max(0, dp[1 - j2][i - 1]) + current_product      # Include both elements
                )
      
        # Return the maximum dot product using all available elements
        return dp[(max_size)%2][min_size]
    # 308ms
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        @lru_cache(None)
        def dp(i, j):
            if i == n or j == m:
                return -math.inf

            # Take both
            take = nums1[i] * nums2[j]
            next_val = dp(i + 1, j + 1)
            if next_val > 0:
                take += next_val

            # Skip one element
            skip1 = dp(i + 1, j)
            skip2 = dp(i, j + 1)

            return max(take, skip1, skip2)

        return dp(0, 0)

    
sol = Solution()
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
sol.maxDotProduct(nums1, nums2)