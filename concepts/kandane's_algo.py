from typing import List
from math import inf
class Solution:
    def minSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        min_sum = inf

        for num in nums:
            curr_sum += num

            min_sum = min(min_sum, curr_sum)

            if curr_sum > 0:
                curr_sum = 0

        return min_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -inf

        for num in nums:
            curr_sum += num

            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum