# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01
from typing import List
class Solution:
    # 0ms
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        rest = nums[1:]
        rest.sort()
        return first + rest[0] + rest[1]

    # 3ms
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(1, n-1):
            min_j = min(nums[i+1:])
            ans = min(ans, nums[0] + nums[i] + min_j)

        return ans
    
sol = Solution()
nums = [1,2,3,12]
nums = [1, 100, 2, 3]
print(sol.minimumCost(nums))