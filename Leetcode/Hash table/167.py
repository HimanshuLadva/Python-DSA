# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num]+1, i+1]

            lookup[num] = i