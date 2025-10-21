# https://leetcode.com/problems/contains-duplicate?envType=problem-list-v2&envId=array
# Contains Duplicate

from typing import List

class Solution:
    def containsDuplicatev1(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
            if lookup[num] > 1:
                return True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)
        if len(new_set) != len(nums):
            return True
        return False
    
s = Solution()
nums = [1,2,3,1]
# nums = [1,2,3,4]
print(s.containsDuplicate(nums))