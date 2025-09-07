# https://leetcode.com/problems/is-subsequence?envType=problem-list-v2&envId=two-pointers
from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:        
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i != len(s):
            return False
        
        return True
    
s1 = Solution()
# s = "abc"
# t = "ahbgdc"
# s = "ab"
# t = "baab"
s = "aza"
t = "abzba"
print(s1.isSubsequence(s, t))