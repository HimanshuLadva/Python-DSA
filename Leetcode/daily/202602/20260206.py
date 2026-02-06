# https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        l = 0
        for r in range(n):
            if nums[r] > nums[l] * k:
                l += 1
        return l
    # 140ms
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # min * k >= max
        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[left] * k >= nums[right]:
                right += 1
            ans = min(ans, n - (right - left)) 

        return ans

sol = Solution()
nums = [4,6]
nums = [1,6,2,9]
nums = [2,1,5]
nums = [33,6,19]
nums = [1, 10, 100, 1000]
k = 5

# when all element is zero then answer is n - 1

print(sol.minRemoval(nums, k))    