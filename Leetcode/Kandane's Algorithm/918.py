# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

from typing import List
from math import inf
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
            curr_max = -inf
            max_sum = -inf
            curr_min = inf
            min_sum = inf
            total_sum = 0
    
            for num in nums:
                curr_max += num
                max_sum = max(curr_max, max_sum)

                if curr_max < 0:
                     curr_max = 0

                curr_min += num
                min_sum = min(curr_min, min_sum)

                if curr_min > 0:
                     curr_min = 0

                total_sum += num
    
            if total_sum == min_sum:
                return max_sum
    
            return max(max_sum, total_sum - min_sum)
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = -inf
        max_sum = -inf
        curr_min = inf
        min_sum = inf
        total_sum = 0

        for num in nums:

            curr_max = max(num, curr_max + num)
            max_sum = max(curr_max, max_sum)

            curr_min = min(num, curr_min + num)
            min_sum = min(curr_min, min_sum)

            total_sum += num

        if total_sum == min_sum:
            return max_sum

        return max(max_sum, total_sum - min_sum)

sol = Solution()
print(sol.maxSubarraySumCircular(nums = [1,-2,3,-2]))
print(sol.maxSubarraySumCircular(nums = [5,-3, 5]))
print(sol.maxSubarraySumCircular(nums = [5,-1,-2,-3,5]))