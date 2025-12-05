# https://leetcode.com/problems/count-partitions-with-even-sum-difference?envType=daily-question&envId=2025-12-05

from typing import List
class Solution:
    # 0ms
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums) % 2: return 0
        return len(nums) - 1
    
    # 3ms
    def countPartitionsV1(self, nums: List[int]) -> int:
        nlen = len(nums)
        count = 0
        for i in range(nlen-1):
            if (sum(nums[:i+1]) - sum(nums[i+1:nlen])) % 2 == 0:
                count += 1
        return count
    