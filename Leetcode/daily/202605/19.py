# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2026-05-19

from typing import List 
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        result = list(set(nums1) & set(nums2))
        return -1 if len(result) == 0 else min(result)