# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three?envType=daily-question&envId=2025-11-22

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            temp = num % 3
            if temp > 3:
                count += temp
            elif temp != 0:
                count += 1
        return count
    
sol = Solution()
nums = [1,2,3,4]
sol.minimumOperations(nums)