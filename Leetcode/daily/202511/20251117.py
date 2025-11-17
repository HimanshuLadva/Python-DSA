# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away?envType=daily-question&envId=2025-11-17

from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -float('inf')
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev <= k:
                    return False
                prev = i
        return True
    
    # 11ms
    def kLengthApartV1(self, nums: List[int], k: int) -> bool:
        if nums and not k:
            return True
        lookup = {}
        numslen = len(nums)

        for i in range(numslen):
            if nums[i] == 1:
                lookup[i] = 1

        prev = 0
        for x in lookup:
            if prev and (x - prev) <= k:
                return False
            prev = x if x else 1

        return True        
    
sol = Solution()
nums = [1,0,0,0,1,0,0,1]
nums = [0,1, 0,0,1,0,0,1]
nums = [1,0,0,1,0,1]
# nums = [1,0,1]
# nums = [1,1,1,1,1]
k = 2
# k = 0
print(sol.kLengthApart(nums, k))