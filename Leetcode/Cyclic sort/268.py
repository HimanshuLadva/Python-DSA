# https://leetcode.com/problems/missing-number/description/

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i]

            if correct_idx < n and nums[i] != nums[correct_idx]:
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
            else:
                i += 1


        for i in range(n):
            if nums[i] != i:
                return i 
        return n

sol = Solution()
sol.missingNumber(nums = [3,0,1])