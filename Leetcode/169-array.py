# https://leetcode.com/problems/majority-element?envType=problem-list-v2&envId=array
# Majority Element
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
        
        # max_pair = max(lookup.items(), key=lambda x: x[1])
        # max_value = max(lookup, key=lookup.get)

        return max(lookup, key=lookup.get)
    
s = Solution()
nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))