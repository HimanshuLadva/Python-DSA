# https://leetcode.com/problems/first-letter-to-appear-twice
# First Letter to Appear Twice
from typing import List

class Solution(object):
    def repeatedCharacter(self, s):
        lookup = {}
        for x in s:
            if x not in lookup:
                lookup[x] = 0
             
            lookup[x] += 1
            if lookup[x] >= 2:
                return x                

        return None

sol = Solution()
s = "abccbaacz"
sol.repeatedCharacter(s)