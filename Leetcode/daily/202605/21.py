# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2026-05-21
from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hash_arr1 = set()
        hash_arr2 = set()

        for ele in arr1:
            temp = list(str(ele))
            for i,x in enumerate(temp):
                hash_arr1.add(int("".join(temp[:i+1])))
        
        for ele in arr2:
            temp = list(str(ele))
            for i,x in enumerate(temp):
                hash_arr2.add(int("".join(temp[:i+1])))
        
        # print(hash_arr1, hash_arr2, list(hash_arr1 & hash_arr2))
        final_arr = list(hash_arr1 & hash_arr2)

        if len(final_arr):
            return len(list(str(max(final_arr))))
        else:
            return 0
        
sol = Solution()
# print(sol.longestCommonPrefix([100,1,2,3,4,5], [1000,6,7,8,9,71]))
print(sol.longestCommonPrefix([13,27,45], [21,27,48]))
        