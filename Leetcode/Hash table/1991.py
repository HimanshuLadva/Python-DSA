# https://leetcode.com/problems/find-the-middle-index-in-array/description/

from typing import List
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        prev_sum = 0

        for i, num in enumerate(nums):
            if prev_sum == all_sum - num - prev_sum:
                return i
            prev_sum += num
            
        return -1

sol = Solution()
sol.findMiddleIndex(nums = [2,3,-1,8,4])