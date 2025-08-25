# https://leetcode.com/problems/missing-number?envType=problem-list-v2&envId=array
# Missing Number
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i,num in enumerate(nums):
            if i != num:
                return i
            
        return i+1

s = Solution()    
nums = [3,0,1]
# nums = [1]
nums = [0,1]
print(s.missingNumber(nums))
