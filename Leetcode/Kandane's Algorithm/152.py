# https://leetcode.com/problems/maximum-product-subarray/description/https://leetcode.com/problems/maximum-product-subarray/description/

from typing import List
from math import inf
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        max_product = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            max_product = max(curr_max, max_product)

        return max_product

sol = Solution()
# sol.maxProduct(nums = [2,3,-2,4])
sol.maxProduct(nums = [-3,-1,-1])
        