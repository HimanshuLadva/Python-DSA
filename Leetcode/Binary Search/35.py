# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=binary-search

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0 
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left

sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))