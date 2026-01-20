# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20
#topic - << operator in py
from typing import List
class Solution:
    # 0ms
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums

    # 147ms
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                i = 0
                while True:
                    if i | (i+1) == num:
                        ans.append(i)
                        break
                    i += 1

        return ans
    
sol = Solution()
nums = [2,3,5,7]
sol.minBitwiseArray(nums)