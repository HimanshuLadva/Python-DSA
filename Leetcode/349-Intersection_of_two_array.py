# https://leetcode.com/problems/intersection-of-two-arrays?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f_len = len(nums1)
        s_len = len(nums2)
        i = 0
        j = 0

        nums1.sort()
        nums2.sort()
        ans = set()

        while i < f_len and j < s_len:
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        result = []
        for x in ans:
            result.append(x)

        return result
    
    def intersectionV2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for num1 in nums1:
            if num1 in nums2:
                ans.add(num1)
        return list(ans)
    
    def intersectionV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for num1 in nums1:
            if num1 in nums2:
                ans.add(num1)
        return list(ans)
    
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection(nums1, nums2))