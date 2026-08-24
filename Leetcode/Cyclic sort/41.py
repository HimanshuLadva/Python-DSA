# https://leetcode.com/problems/first-missing-positive/

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] <= 0:
                i += 1
                continue
            idx = nums[i] - 1

            if idx < n and nums[i] != nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
            else:
                i += 1

        # print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1
            
        return 0

sol = Solution()
print(sol.firstMissingPositive(nums = [3,4,0,2]))