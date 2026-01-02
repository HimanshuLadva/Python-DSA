# https://leetcode.com/problems/n-repeated-element-in-size-2n-array?envType=daily-question&envId=2026-01-02

from typing import List
from collections import Counter
class Solution:
    # 0ms
    def repeatedNTimes(self, nums: List[int]) -> int:
        lookup = {}
        for i in nums:
            if i in lookup:
                return i
            lookup[i] = 1
        return -1
    
    # 12ms
    def repeatedNTimes(self, nums: List[int]) -> int:
        k = len(nums) // 2
        myDict = Counter(nums)
        for key,val in myDict.items():
            if val==k:
                return key
        return -1
    
    # 19ms
    def repeatedNTimes(self, nums: List[int]) -> int:
        lookup = {}
        n = len(nums)
        print(n)
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1

        # print(lookup)
        for i in lookup:
            if lookup[i] == (n // 2):
                return i
        return 0
    
sol = Solution()
nums = [5,1,5,2,5,3,5,4]
print(sol.repeatedNTimes(nums))