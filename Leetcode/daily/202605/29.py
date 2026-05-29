# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/?envType=daily-question&envId=2026-05-29

from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = float('inf')

        for n in nums:
            curr = 0
            while n:
                curr = n % 10
                n //= 10
            
            minimum = min(minimum, int(curr))
        
        return minimum
    
    # 7ms
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = float('inf')
        for i in range(n):
            nums[i] = sum([int(x) for x in str(nums[i])])

            if nums[i] < minimum:
                minimum = nums[i]

        return minimum
        
sol = Solution()
print(sol.minElement(nums = [10,12,13,14]))
