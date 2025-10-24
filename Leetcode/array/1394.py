# https://leetcode.com/problems/find-lucky-integer-in-an-array?envType=problem-list-v2&envId=counting

from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lookup = {}
        arr.sort()
        for x in arr:
            if x not in lookup:
                lookup[x] = 0
            lookup[x] += 1
        
        result = -1
        for x in lookup:
            if x == lookup[x]:
                result = x
        return result
      
sol = Solution()
arr = [2,2,3,4]
sol.findLucky(arr)