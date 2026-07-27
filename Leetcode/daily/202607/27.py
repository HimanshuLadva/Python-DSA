from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[-1]-1) * (nums[-2]-1), max((nums[0]-1) * (nums[1]-1), (nums[-1]-1) * (nums[0]-1)))

sol = Solution()
print(sol.maxProduct(nums = [3,4,5,2]))