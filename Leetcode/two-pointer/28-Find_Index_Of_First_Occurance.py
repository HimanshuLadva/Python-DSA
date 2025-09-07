# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string?envType=problem-list-v2&envId=two-pointers

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle)

        while end < len(haystack)+1:
            substr = haystack[start:end]
            
            if substr == needle:
                return start
            start += 1
            end += 1

        return -1
    
haystack = "sadbutsad"
needle = "sad"
s = Solution()
print(s.strStr(haystack, needle))