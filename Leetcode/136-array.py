# Single Number
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = {}
        for x in nums:
            if x not in lookup:
                lookup[x] = 0
            lookup[x] += 1

        for key,value in lookup.items():
            if value == 1:
                return key
        
s = Solution()
nums = [4,1,2,1,2]
num = s.singleNumber(nums)
print(num)