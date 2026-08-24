# https://leetcode.com/problems/set-mismatch/description/
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i] - 1

            if correct_idx < n and nums[i] != nums[correct_idx]:
                nums[i],nums[correct_idx]=nums[correct_idx],nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return [nums[i], i+1]

        return []

sol = Solution()
print(sol.findErrorNums(nums = [1,2,2,4]))