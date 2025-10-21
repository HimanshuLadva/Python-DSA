# https://leetcode.com/problems/merge-sorted-array?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
    
        nums1.extend(nums2)
        nums1.sort()

    def mergeV1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = [x for i,x in enumerate(nums1) if i < m]
        nums2 = [x for i,x in enumerate(nums2) if i < n]
    
        for x in nums2:
            nums1.append(x)
            
        nums1.sort()
    
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [1]
# m = 0
# nums2 = [1]
# n = 1
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
print(s.merge(nums1,m,nums2,n))