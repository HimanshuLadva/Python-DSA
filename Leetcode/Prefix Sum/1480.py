# https://leetcode.com/problems/running-sum-of-1d-array/?envType=problem-list-v2&envId=prefix-sum

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        return prefix