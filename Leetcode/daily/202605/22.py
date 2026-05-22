# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-22

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if num == target:
                return i
                
        return -1
        