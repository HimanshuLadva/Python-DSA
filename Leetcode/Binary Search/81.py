# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/?envType=problem-list-v2&envId=binary-search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False