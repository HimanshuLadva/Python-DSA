# https://leetcode.com/problems/separate-the-digits-in-an-array/?envType=daily-question&envId=2026-05-11
from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num > 9:
                res += list(int(i) for i in str(num))
            else:
                res.append(num)
        return res

sol = Solution()
print(sol.separateDigits(nums = [13,25,83,77]))