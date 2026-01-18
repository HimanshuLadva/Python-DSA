# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k?envType=daily-question&envId=2025-11-27
# #learntopic

from typing import List
from itertools import accumulate
class Solution:
    # 535ms
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        dp = [float('-inf')] * (len(nums)+1)
        for i in range(k, len(nums)+1):
            dp[i] = (prefix_sums[i] - prefix_sums[i-k]) + max(0, dp[i-k])
        return max(dp)
    
    # 535ms
    def maxSubarraySumV1(self, nums: List[int], k: int) -> int:
        # Build prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        # Track minimum prefix for each remainder group
        max_sum = float('-inf')
        min_prefix = {}
        for r in range(k):
            min_prefix[r] = float('inf')
        
        # Single pass through prefix array
        for i in range(len(prefix)):
            group = i % k
            
            if min_prefix[group] != float('inf'):
                current_sum = prefix[i] - min_prefix[group]
                max_sum = max(max_sum, current_sum)
            
            min_prefix[group] = min(min_prefix[group], prefix[i])
        
        return max_sum
    
    # TLE
    def maxSubarraySumV1(self, nums: List[int], k: int) -> int:
        numslen = len(nums)

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        max_sum = float('-inf')
        temp = k
        count = 1
        while temp <= numslen:
            for i in range(numslen):
                if temp+i <= numslen:
                    curr_sum = prefix[temp + i] - prefix[i]
                    max_sum = max(curr_sum, max_sum)

            count += 1
            temp = k*count
        return max_sum
    
    # time limit exceeded
    def maxSubarraySumV1(self, nums: List[int], k: int) -> int:
        temp = k
        numslen = len(nums)
        sum_arr = []
        count = 1
        while temp <= numslen:
            for i in range(numslen):
                if temp+i <= numslen:
                    sum_arr.append(sum(nums[i:temp+i]))
            count += 1
            temp = k*count
        return max(sum_arr)
    
sol = Solution()
nums = [-1,-2,-3,-4,-5]
k = 4
nums = [-5,1,2,-3,4]
k = 2
nums = [2,0,10]
k = 1
print(sol.maxSubarraySum(nums, k))