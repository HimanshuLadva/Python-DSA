# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array?envType=problem-list-v2&envId=array
# Find All Numbers Disappeared in an Array
# used Cyclic Sort / Index Mapping 
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [i + 1 for i, num in enumerate(nums) if num > 0]
    
    def findDisappearedNumbersV1(self, nums: List[int]) -> List[int]:
        nums_set= set(nums)
        return [x for x in range(1, len(nums)+1) if x not in nums_set]
    
s = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
print(s.findDisappearedNumbers(nums))