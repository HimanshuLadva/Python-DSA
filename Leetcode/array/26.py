# Remove Duplicates from Sorted Array
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lookup = {}
        for x in nums:
            if x not in lookup:
                lookup[x] = 0
            lookup[x] += 1 

        index = 0
        for x in lookup:
            nums[index] = x
            index += 1
        return index
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = s.removeDuplicates(nums)
print(k)
print(nums[:k])