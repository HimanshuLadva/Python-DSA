# https://leetcode.com/problems/two-sum?envType=problem-list-v2&envId=hash-table
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)

        for i,num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target- num], i]
            lookup[num] = i
    
sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))