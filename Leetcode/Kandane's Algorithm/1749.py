# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi = 0
        mini = 0
        total_sum = 0

        for num in nums:
            total_sum += num

            if total_sum > maxi:
                maxi = total_sum
            if total_sum < mini:
                mini = total_sum

        return maxi - mini
    
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = ans = 0

        for num in nums:
            max_sum = max(0, max_sum + num)
            min_sum = min(0, min_sum + num)

            ans = max(ans, max_sum, abs(min_sum))

        return ans

sol = Solution()
# print(sol.maxAbsoluteSum(nums = [1,-3,2,3,-4]))
print(sol.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2]))