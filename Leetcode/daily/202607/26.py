# https://leetcode.com/problems/maximum-product-of-three-numbers/?envType=daily-question&envId=2026-07-26
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

sol = Solution()
sol.maximumProduct([-100,-98,-1,2,3,4])