# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums)
        ans = []

        for i in range(1, n+1):
            if i not in s:
                ans.append(i)
                # print(i)
        return ans

sol = Solution()
# sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])
sol.findDisappearedNumbers(nums = [1,1])