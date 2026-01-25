# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        
        for i in range(len(nums)-k+1):
            min_diff = min(min_diff,nums[i+k-1] - nums[i])
        
        return min_diff
    # 6ms
    def minimumDifferenceV1(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = k - 1
        min_e = float('inf')
        while j < n:
            if nums[j] - nums[i] < min_e:
                min_e = nums[j] - nums[i]
            i += 1
            j += 1
        return min_e
    
sol = Solution()
nums = [9,4,1,7]
k = 2
print(sol.minimumDifference(nums, k))