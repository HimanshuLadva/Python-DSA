# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville?envType=daily-question&envId=2025-10-31

from typing import List
from collections import Counter
class Solution:
    # 0ms
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [x for x in counter if counter[x] == 2]
    
    # 3ms
    def getSneakyNumbersV1(self, nums: List[int]) -> List[int]:
        lookup = {}
        result = []
        for x in nums:
            if x not in lookup:
                lookup[x] = 0
            lookup[x] += 1

            if lookup[x] == 2:
                result.append(x)
    
        return result

sol = Solution()
nums = [0,1,1,0]
nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(sol.getSneakyNumbers(nums))        