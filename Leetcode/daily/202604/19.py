# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/?envType=daily-question&envId=2026-04-19
from typing import List
from math import inf
import bisect
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        nums2.sort()
        # print(f"nums1 = {nums1}")
        # print(f"nums2 = {nums2}")

        res = 0
        for i in range(m):
            pos = bisect.bisect_left(nums2, nums1[i])
            # print(f"pos = {pos}")
            res = max(res, (n - pos - 1) - i)
        
        return res
    
    # TLE
    def maxDistanceV1(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = -inf
        
        for i in range(m):
            for j in range(i, n):
                if nums1[i] <= nums2[j]:
                    res = max(res, j - i)

        return res if res != -inf else 0
    
sol = Solution()
print(sol.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
print(sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
print(sol.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))