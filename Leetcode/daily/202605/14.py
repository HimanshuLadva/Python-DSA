# https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14
from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        max_ele = nums[-1]

        if len(nums) != max_ele + 1 or nums[-1] != nums[-2]:
            return False
        
        for i in range(max_ele - 1):
            if nums[i] != i+1:
                return False
            
        return True
    def isGood(self, nums: List[int]) -> bool:
        max_ele = max(nums)
        nums.sort()
        temp_arr = []

        for i in range(1,max_ele+1):
            temp_arr.append(i)
        
        temp_arr.append(i)
        return temp_arr == nums
        