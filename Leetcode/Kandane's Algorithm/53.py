from typing import List
from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -inf

        for num in nums:
            curr_sum += num

            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum

    def maxSubArrayV1(self, nums: List[int]) -> int:
        curr_sum = -inf
        max_sum = -inf

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        # print(max_sum)
        return max_sum

sol = Solution()
sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])