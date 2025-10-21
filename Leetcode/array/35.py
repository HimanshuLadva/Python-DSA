# Search Insert Position
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0
        
        for i,num in enumerate(nums):
            if target > num:
                position = (i+1)
            
        return position
    
s = Solution()
nums = [1,3,5,6] 
target = 7
result = s.searchInsert(nums, target)
print(result)