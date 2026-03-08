# https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08

from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        #implogic - find all combination of 0 and 1 of length of n
        for i in range(2**n):
            b = format(i, f'0{n}b')
            if b not in nums:
                return b
        return ""
    
sol = Solution()
nums = ["111","011","001"]
print(sol.findDifferentBinaryString(nums))