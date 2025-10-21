# https://leetcode.com/problems/move-zeroes?envType=problem-list-v2&envId=array
# Move Zeroes
from typing import List

class Solution:
    def moveZeroesV1(self, nums: List[int]) -> None:
        pre_len = len(nums)
        nums = [x for x in nums if x != 0]
        diff = pre_len - len(nums)

        while diff != 0:
            nums.append(0)
            diff -= 1

        print(nums)

    def moveZeroesV2(self, nums: List[int]) -> None:        
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)

        print(nums)
    
    def moveZeroes(self, nums: List[int]) -> None:        
        i = 0
        j = 1
        nums_len = len(nums)

        while i < j and j < nums_len:
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
            elif nums[i] != 0:
                i += 1                 
            j += 1

            if i == nums_len or j == nums_len:
                break


    
s = Solution()
nums = [0,1,0,3,12]
# nums = [0]
# nums = [4,2,4,0,0,3,0,5,1,0]
# nums = [1,0,3,0,6,0]
s.moveZeroes(nums)