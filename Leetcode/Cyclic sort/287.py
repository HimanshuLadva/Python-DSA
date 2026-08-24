# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            idx = nums[i] - 1

            if idx < n and nums[idx] != nums[i]:
                nums[i],nums[idx] = nums[idx],nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]

        return 0

sol = Solution()
print(sol.findDuplicate(nums = [1,3,4,2,2]))