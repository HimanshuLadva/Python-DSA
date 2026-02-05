# https://leetcode.com/problems/transformed-array/?envType=daily-question&envId=2026-02-05

from typing import List
class Solution:
    # 66ms
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i,num in enumerate(nums):
            if num == 0:
                result.append(num)
            else:
                result.append(nums[(i + num) % n])
            
        return result
    # 63ms
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(nums[(i+nums[i]) % n])
            elif nums[i] < 0:
                result.append(nums[i-abs(nums[i]) % n])
            else:
                result.append(0)    
            
        return result

sol = Solution()
nums = [3,-2,1,1]
nums = [-1,4,-1]
nums = [-9,0]
print(sol.constructTransformedArray(nums))