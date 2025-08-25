# Two sum
from typing import List

class Solution:
    """ def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,item in enumerate(nums):
            print(f"for index {index}")
            for x in range(index + 1, len(nums)):
                print(f"index {x} ", end= ' ')
                if nums[x] + nums[index] == target:
                    return [index, x] """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index,num in enumerate(nums): 
            if target - num in lookup:
                return [lookup[target - num], index]
            lookup[num] = index
            
s = Solution()
result = s.twoSum([3,2,3], 6)
print(f"result is {result}")