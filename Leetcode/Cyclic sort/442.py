# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0 
        while i < n:
            idx = nums[i] - 1

            if idx < n and nums[i] != nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
            else:
                i += 1

        # print(nums)

        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])

        return ans

sol = Solution()
print(sol.findDuplicates(nums = [4,3,2,7,8,2,3,1]))