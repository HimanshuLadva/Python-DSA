# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/?envType=daily-question&envId=2026-01-22
#howtowork
from typing import List
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return True
            return False
        
        operations = 0
        
        while is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            
            # Find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            
            # Replace the pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            operations += 1
        
        return operations

sol = Solution()
nums = [5,2,3,1]
sol.minimumPairRemoval(nums)